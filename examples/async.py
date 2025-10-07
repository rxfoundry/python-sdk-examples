import argparse
import rxfoundry.clients.swifty_api
from rxfoundry.clients.swifty_api import PatientActivityNotification, PatientData, \
    PatientActivityNotificationActivityData
from rxfoundry.clients.swifty_api.rest import ApiException
from authentication import get_auth_tokens, get_user_info

def add_patient_data(host: str, token: str):
    configuration = rxfoundry.clients.swifty_api.Configuration(
        host=f"{host}/api", access_token=token
    )
    with rxfoundry.clients.swifty_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_api.AsyncApi(api_client)
        try:
            patient_activity_notification = PatientActivityNotification(
                object_type="patient",
                external_patient_id="7654321",
                external_system_slug="CPD-FRONTEND",
                action = "created",
                activity_data=PatientActivityNotificationActivityData(
                    PatientData(
                        first_name="Jane",
                        last_name="Doe",
                        gender_assigned_at_birth="F",
                        date_of_birth="1970-04-25",
                        email="ptindall+john+doe@gmail.com",
                        object_type="patient",
                        primary_phone="512 605-9456"
                    )
                )
            )
            api_response = api_instance.create_patient_activity(
                patient_activity_notification=patient_activity_notification
            )
            return api_response
        except ApiException as e:
            print("Exception when calling AsyncApi->add_patient_data: %s\n" % e)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="The host to authenticate against.")
    parser.add_argument("username", help="The username for authentication.")
    parser.add_argument("password", help="The password for authentication.")
    args = parser.parse_args()

    token_response = get_auth_tokens(args.host, args.username, args.password)
    print(token_response)
    add_patient_data_response = add_patient_data(args.host, token_response.access_token)
    print(add_patient_data_response)