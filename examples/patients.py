import argparse
import rxfoundry.clients.swifty_api
from rxfoundry.clients.swifty_api.rest import ApiException
from authentication import get_auth_tokens, get_user_info


def get_patients(host: str, token: str, q: str):
    configuration = rxfoundry.clients.swifty_api.Configuration(
        host=f"{host}/api", access_token=token
    )
    with rxfoundry.clients.swifty_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_api.PatientApi(api_client)
        try:
            api_response = api_instance.get_patients(q="Paul Tindall")
            return api_response
        except ApiException as e:
            print("Exception when calling DefaultApi->get_patients: %s\n" % e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="The host to authenticate against.")
    parser.add_argument("username", help="The username for authentication.")
    parser.add_argument("password", help="The password for authentication.")
    args = parser.parse_args()

    token_response = get_auth_tokens(args.host, args.username, args.password)
    print(token_response)
    patients_response = get_patients(
        args.host, token_response.access_token, "Paul Tindall 1970-04-25"
    )
    for patient in patients_response:
        print(patient)
