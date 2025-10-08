import argparse
import rxfoundry.clients.swifty_api
from rxfoundry.clients.swifty_api import PatientActivityNotification, PatientData, PatientAddressData, PatientInsuranceData, PatientActivityNotificationActivityData
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
                external_patient_id="7654322",
                external_system_slug="CPD-FRONTEND",
                action = "created",
                activity_data=PatientActivityNotificationActivityData(
                    PatientData(
                        first_name="John",
                        last_name="Doe",
                        gender_assigned_at_birth="M",
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

def update_patient_data(host: str, token: str):
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
                action = "updated",
                activity_data=PatientActivityNotificationActivityData(
                    PatientData(
                        first_name="Jane",
                        last_name="Sanchez",
                        gender_assigned_at_birth="F",
                        date_of_birth="1970-04-25",
                        email="ptindall+jane+doe@gmail.com",
                        object_type="patient",
                        primary_phone="512 349-0404"
                    )
                )
            )
            api_response = api_instance.create_patient_activity(
                patient_activity_notification=patient_activity_notification
            )
            return api_response
        except ApiException as e:
            print("Exception when calling AsyncApi->add_patient_data: %s\n" % e)

def add_patient_address_data(host: str, token: str):
    configuration = rxfoundry.clients.swifty_api.Configuration(
        host=f"{host}/api", access_token=token
    )
    with rxfoundry.clients.swifty_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_api.AsyncApi(api_client)
        try:
            patient_activity_notification = PatientActivityNotification(
                object_type="address",
                external_patient_id="7654322",
                external_system_slug="CPD-FRONTEND",
                action = "created",
                activity_data=PatientActivityNotificationActivityData(
                    PatientAddressData(
                        address_line_one="123 Main Street",
                        city="Boston",
                        state_province="MA",
                        postal_code="02116",
                        object_type="address",
                        country_code="US",
                    )
                )
            )
            api_response = api_instance.create_patient_activity(
                patient_activity_notification=patient_activity_notification
            )
            return api_response
        except ApiException as e:
            print("Exception when calling AsyncApi->add_patient_data: %s\n" % e)

def update_patient_address_data(host: str, token: str):
    configuration = rxfoundry.clients.swifty_api.Configuration(
        host=f"{host}/api", access_token=token
    )
    with rxfoundry.clients.swifty_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_api.AsyncApi(api_client)
        try:
            patient_activity_notification = PatientActivityNotification(
                object_type="address",
                external_patient_id="7654322",
                external_system_slug="CPD-FRONTEND",
                action = "updated",
                activity_data=PatientActivityNotificationActivityData(
                    PatientAddressData(
                        address_line_one="125 Main Street",
                        city="Boston",
                        state_province="MA",
                        postal_code="02116",
                        object_type="address",
                        country_code="US",
                    )
                )
            )
            api_response = api_instance.create_patient_activity(
                patient_activity_notification=patient_activity_notification
            )
            return api_response
        except ApiException as e:
            print("Exception when calling AsyncApi->add_patient_data: %s\n" % e)

def add_patient_insurance_data(host: str, token: str):
    configuration = rxfoundry.clients.swifty_api.Configuration(
        host=f"{host}/api", access_token=token
    )
    with rxfoundry.clients.swifty_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_api.AsyncApi(api_client)
        try:
            patient_activity_notification = PatientActivityNotification(
                object_type="insurance",
                external_patient_id="7654321",
                external_system_slug="CPD-FRONTEND",
                action = "created",
                activity_data=PatientActivityNotificationActivityData(
                    PatientInsuranceData(
                        member_id="123456789",
                        rx_group="RX1234",
                        rx_bin="012345",
                        rx_pcn="1234567",
                        object_type="insurance",
                    )
                )
            )
            api_response = api_instance.create_patient_activity(
                patient_activity_notification=patient_activity_notification
            )
            return api_response
        except ApiException as e:
            print("Exception when calling AsyncApi->add_patient_insurance_data: %s\n" % e)


def update_patient_insurance_data(host: str, token: str):
    configuration = rxfoundry.clients.swifty_api.Configuration(
        host=f"{host}/api", access_token=token
    )
    with rxfoundry.clients.swifty_api.ApiClient(configuration) as api_client:
        api_instance = rxfoundry.clients.swifty_api.AsyncApi(api_client)
        try:
            patient_activity_notification = PatientActivityNotification(
                object_type="insurance",
                external_patient_id="7654321",
                external_system_slug="CPD-FRONTEND",
                action = "updated",
                activity_data=PatientActivityNotificationActivityData(
                    PatientInsuranceData(
                        member_id="123456789",
                        rx_group="RX1234",
                        rx_bin="543210",
                        rx_pcn="754321",
                        object_type="insurance",
                    )
                )
            )
            api_response = api_instance.create_patient_activity(
                patient_activity_notification=patient_activity_notification
            )
            return api_response
        except ApiException as e:
            print("Exception when calling AsyncApi->add_patient_insurance_data: %s\n" % e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("host", help="The host to authenticate against.")
    parser.add_argument("username", help="The username for authentication.")
    parser.add_argument("password", help="The password for authentication.")
    args = parser.parse_args()

    token_response = get_auth_tokens(args.host, args.username, args.password)
    print(token_response)

    # add_patient_data_response = add_patient_data(args.host, token_response.access_token)
    # print(add_patient_data_response)

    # add_patient_address_data_response = add_patient_address_data(args.host, token_response.access_token)
    # print(add_patient_address_data_response)

    # add_patient_insurance_data_response = add_patient_insurance_data(args.host, token_response.access_token)
    # print(add_patient_insurance_data_response)

    # update_patient_data_response = update_patient_data(args.host, token_response.access_token)
    # print(update_patient_data_response)

    # update_patient_address_data_response = update_patient_address_data(args.host, token_response.access_token)
    # print(update_patient_address_data_response)

    # update_patient_insurance_data_response = update_patient_insurance_data(args.host, token_response.access_token)
    # print(update_patient_insurance_data_response)







