import rxfoundry.clients.swifty_oauth_api
import argparse
from rxfoundry.clients.swifty_oauth_api import TokenResponse, UserInfoResponse
from rxfoundry.clients.swifty_oauth_api.rest import ApiException


def get_auth_tokens(host: str, username: str, password: str) -> TokenResponse | None:
    configuration = rxfoundry.clients.swifty_oauth_api.Configuration(host=host)
    with rxfoundry.clients.swifty_oauth_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_oauth_api.OAuthApi(api_client)
        get_token_request = rxfoundry.clients.swifty_oauth_api.GetTokenRequest(
            grant_type="password", username=username, password=password
        )

        try:
            api_response = api_instance.get_token(get_token_request)
            return api_response
        except ApiException as e:
            print("Exception when calling DefaultApi->get_token: %s\n" % e)


def get_user_info(token) -> UserInfoResponse | None:
    configuration = rxfoundry.clients.swifty_oauth_api.Configuration(
        host="https://bootstrap.swiftyrx.dev"
    )
    with rxfoundry.clients.swifty_oauth_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_oauth_api.OAuthApi(api_client)

        try:
            api_response = api_instance.get_user_info(
                _headers={"Authorization": f"Bearer {token}"}
            )
            return api_response
        except ApiException as e:
            print("Exception when calling DefaultApi->get_user_info: %s\n" % e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="The host to authenticate against.")
    parser.add_argument("username", help="The username for authentication.")
    parser.add_argument("password", help="The password for authentication.")
    args = parser.parse_args()

    token_response = get_auth_tokens(args.host, args.username, args.password)
    print(token_response)
    user_info = get_user_info(token_response.access_token)
    print(user_info)
