import allure
import pytest

from meme_api_tests.tests.data import payloads

from meme_api_tests.client import allure_annotations


@allure_annotations(
    title="Valid authorization",
    story="Authorization",
    description='This test checks creating a token with valid data name in request',
    severity=allure.severity_level.BLOCKER,
    tag='Positive'
)
@pytest.mark.blocker
def test_get_auth_token_success(post_authorize_endpoint) -> None:
    post_authorize_endpoint.get_token(payloads.valid_auth_payload)
    success, message = post_authorize_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = post_authorize_endpoint.check_response_name_is_(payloads.valid_auth_payload['name'])
    assert success, message


@allure_annotations(
    title="Invalid data name",
    story="Authorization",
    description='This test checks creating a token with invalid data name in request',
    severity=allure.severity_level.BLOCKER
)
@pytest.mark.blocker
@pytest.mark.parametrize("invalid_payload", payloads.invalid_payload_name(), ids=payloads.invalid_payload_name_ids)
def test_get_auth_token_invalid_name(post_authorize_endpoint, invalid_payload: dict) -> None:
    post_authorize_endpoint.get_token(invalid_payload)
    success, message = post_authorize_endpoint.check_status_code_is_(400)
    assert success, message
    success, message = post_authorize_endpoint.check_response_message_is_('400 Bad Request')
    assert success, message


@allure_annotations(
    title="Invalid field in data",
    story="Authorization",
    description='This test checks creating a token with an extra field in request',
    severity=allure.severity_level.BLOCKER
)
@pytest.mark.blocker
def test_get_auth_token_with_invalid_field(post_authorize_endpoint) -> None:
    post_authorize_endpoint.get_token(payloads.invalid_auth_payload)
    success, message = post_authorize_endpoint.check_status_code_is_(400)
    assert success, message
    success, message = post_authorize_endpoint.check_response_message_is_('400 Bad Request')
    assert success, message


@allure_annotations(
    title="Valid token",
    story="Token check",
    description='This test checks token relevance with valid token in request',
    severity=allure.severity_level.MINOR,
    tag='Positive'
)
@pytest.mark.minor
def test_check_valid_auth_token(get_check_token_endpoint, auth_token: str) -> None:
    get_check_token_endpoint.check_token_is_valid(auth_token)
    success, message = get_check_token_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = get_check_token_endpoint.check_response_message_is_("Token is alive")
    assert success, message


@allure_annotations(
    title="Invalid token",
    story="Token check",
    description='This test checks token relevance with invalid token in request',
    severity=allure.severity_level.MINOR,
)
@pytest.mark.minor
def test_check_invalid_auth_token(get_check_token_endpoint) -> None:
    get_check_token_endpoint.check_token_is_valid('invalid_token')
    success, message = get_check_token_endpoint.check_status_code_is_(404)
    assert success, message
    success, message = get_check_token_endpoint.check_response_message_is_("Token not found")
    assert success, message


@allure_annotations(
    title="Valid meme",
    story="Create",
    description='This test checks adding a valid meme object',
    severity=allure.severity_level.CRITICAL,
    tag='Positive'
)
@pytest.mark.critical
def test_create_meme_object(post_meme_endpoint, delete_meme, request, auth_token: str) -> None:
    request.node.meme_id = post_meme_endpoint.create_meme_object(payloads.create_meme, auth_token)
    success, message = post_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = post_meme_endpoint.check_response_url_is_(payloads.create_meme['url'])
    assert success, message


@allure_annotations(
    title="Without authorization",
    story="Create",
    description='This test checks adding a meme object without authorization',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.critical
def test_create_meme_object_without_auth(post_meme_endpoint, delete_meme, request, auth_token: str) -> None:
    request.node.meme_id = post_meme_endpoint.create_meme_object(payloads.create_meme, 'invalid_token')
    success, message = post_meme_endpoint.check_status_code_is_(401)
    assert success, message
    success, message = post_meme_endpoint.check_response_message_is_('Unauthorized')
    assert success, message


@allure_annotations(
    title="Missing mandatory fields",
    story="Create",
    description='This test checks adding a meme object with missing mandatory fields in request payload',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.critical
@pytest.mark.parametrize(
    "invalid_payload",
    payloads.post_fields_binding_validation_payloads(),
    ids=payloads.post_fields_binding_validation_payloads_ids)
def test_create_meme_object_with_missing_fields(post_meme_endpoint, invalid_payload, request,
                                                auth_token: str) -> None:
    request.node.meme_id = post_meme_endpoint.create_meme_object(invalid_payload, auth_token)
    success, message = post_meme_endpoint.check_status_code_is_(400)
    assert success, message
    success, message = post_meme_endpoint.check_response_message_is_('Bad Request')
    assert success, message


@allure_annotations(
    title="Invalid data types",
    story="Create",
    description='This test checks adding a meme object with invalid data types in request payload',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.critical
@pytest.mark.parametrize(
    "invalid_payload",
    payloads.post_invalid_data_types_payloads(),
    ids=payloads.post_invalid_data_types_payloads_ids())
def test_create_meme_object_with_invalid_data_types(post_meme_endpoint, invalid_payload, request,
                                                    auth_token: str) -> None:
    request.node.meme_id = post_meme_endpoint.create_meme_object(invalid_payload, auth_token)
    success, message = post_meme_endpoint.check_status_code_is_(400)
    assert success, message
    success, message = post_meme_endpoint.check_response_message_is_('Bad Request')
    assert success, message


@allure_annotations(
    title="Extra field",
    story="Create",
    description='This test checks adding a meme object with extra field in request payload',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.critical
def test_create_meme_object_with_extra_field(post_meme_endpoint, delete_meme, request, auth_token: str) -> None:
    request.node.meme_id = post_meme_endpoint.create_meme_object(payloads.create_meme_with_an_extra_field, auth_token)
    success, message = post_meme_endpoint.check_status_code_is_(400)
    assert success, message
    success, message = post_meme_endpoint.check_response_message_is_('Bad Request')
    assert success, message


@allure_annotations(
    title="Valid meme",
    story="Get by id",
    description='This test checks getting a valid meme object',
    severity=allure.severity_level.MINOR,
    tag='Positive'
)
@pytest.mark.minor
def test_get_meme_object(get_meme_endpoint, meme_id: int, auth_token: str) -> None:
    get_meme_endpoint.get_meme(meme_id, auth_token)
    success, message = get_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = get_meme_endpoint.check_response_id_is_(meme_id)
    assert success, message


@allure_annotations(
    title="Without authorization",
    story="Get by id",
    description='This test checks getting a meme object without authorization',
    severity=allure.severity_level.MINOR
)
@pytest.mark.minor
def test_get_meme_object_without_auth(get_meme_endpoint, meme_id: int, auth_token: str) -> None:
    get_meme_endpoint.get_meme(meme_id, 'invalid_token')
    success, message = get_meme_endpoint.check_status_code_is_(401)
    assert success, message
    success, message = get_meme_endpoint.check_response_message_is_("Unauthorized")
    assert success, message


@allure_annotations(
    title="Invalid id",
    story="Get by id",
    description='This test checks getting a meme object with invalid id in request payload',
    severity=allure.severity_level.MINOR
)
@pytest.mark.minor
def test_get_meme_object_with_invalid_id(get_meme_endpoint, meme_id: int, auth_token: str) -> None:
    get_meme_endpoint.get_meme(0, auth_token)
    success, message = get_meme_endpoint.check_status_code_is_(404)
    assert success, message
    success, message = get_meme_endpoint.check_response_message_is_("Not Found")
    assert success, message


@allure_annotations(
    title="All valid meme",
    story="Get all",
    description='This test checks getting all valid meme objects',
    severity=allure.severity_level.MINOR,
    tag='Positive'
)
@pytest.mark.minor
def test_get_all_meme_objects(get_all_meme_endpoint, auth_token: str) -> None:
    get_all_meme_endpoint.get_all_meme(auth_token)
    success, message = get_all_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = get_all_meme_endpoint.check_response_is_not_empty()
    assert success, message


@allure_annotations(
    title="Without authorization",
    story="Get all",
    description='This test checks getting all meme objects without authorization',
    severity=allure.severity_level.MINOR
)
@pytest.mark.minor
def test_get_all_meme_objects_without_auth(get_all_meme_endpoint, auth_token: str) -> None:
    get_all_meme_endpoint.get_all_meme('invalid_token')
    success, message = get_all_meme_endpoint.check_status_code_is_(401)
    assert success, message
    success, message = get_all_meme_endpoint.check_response_message_is_("Unauthorized")
    assert success, message


@allure_annotations(
    title="Valid meme",
    story="Update",
    description='This test checks updating a valid meme object',
    tag='Positive'
)
@pytest.mark.parametrize("request_data", payloads.update_params_payloads(), ids=payloads.payload_update_ids)
def test_update_object(update_meme_endpoint, request_data: dict, meme_id: int, auth_token: str) -> None:
    request_data["id"] = meme_id
    update_meme_endpoint.update_meme_object(request_data, meme_id, auth_token)
    success, message = update_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = update_meme_endpoint.check_response_text_is_(request_data['text'])
    assert success, message
    success, message = update_meme_endpoint.check_does_the_answer_hold_a_key_('title')
    assert success, message
    success, message = update_meme_endpoint.check_does_the_answer_hold_a_key_('type')
    assert success, message


@allure_annotations(
    title="Without authorization",
    story="Update",
    description='This test checks updating a meme object without authorization',
)
def test_update_object_without_auth(update_meme_endpoint, meme_id: int, auth_token: str) -> None:
    update_meme_endpoint.update_meme_object(payloads.valid_update_payload(meme_id), meme_id, 'invalid_token')
    success, message = update_meme_endpoint.check_status_code_is_(401)
    assert success, message
    success, message = update_meme_endpoint.check_response_message_is_("Unauthorized")
    assert success, message


@allure_annotations(
    title="Invalid id",
    story="Update",
    description='This test checks updating a meme object with invalid id in request payload',
)
def test_update_object_with_invalid_id(update_meme_endpoint, meme_id: int, auth_token: str) -> None:
    update_meme_endpoint.update_meme_object(payloads.valid_update_payload(meme_id), 0, auth_token)
    success, message = update_meme_endpoint.check_status_code_is_(404)
    assert success, message
    success, message = update_meme_endpoint.check_response_message_is_("Not Found")
    assert success, message


@allure_annotations(
    title="Invalid data types",
    story="Update",
    description='This test checks updating a meme object with invalid data types in request payload',
)
@pytest.mark.parametrize(
    "invalid_data_types",
    payloads.put_invalid_data_types_payloads(),
    ids=payloads.put_invalid_data_types_payloads_ids())
def test_update_object_with_invalid_data_types(update_meme_endpoint, invalid_data_types: dict, meme_id: int,
                                               auth_token: str) -> None:
    update_meme_endpoint.update_meme_object(invalid_data_types, meme_id, auth_token)
    success, message = update_meme_endpoint.check_status_code_is_(400)
    assert success, message
    success, message = update_meme_endpoint.check_response_message_is_("Bad Request")
    assert success, message


@allure_annotations(
    title="Missing mandatory fields",
    story="Update",
    description='This test checks updating a meme object with missing mandatory fields in request payload',
)
@pytest.mark.parametrize(
    "missing_data_fields",
    payloads.put_fields_binding_validation_payloads(),
    ids=payloads.put_fields_binding_validation_payloads_ids)
def test_update_object_with_missing_mandatory_fields(update_meme_endpoint, missing_data_fields: dict, meme_id: int,
                                                     auth_token: str) -> None:
    if "id" in missing_data_fields:
        missing_data_fields["id"] = meme_id
    update_meme_endpoint.update_meme_object(missing_data_fields, meme_id, auth_token)
    success, message = update_meme_endpoint.check_status_code_is_(400)
    assert success, message
    success, message = update_meme_endpoint.check_response_message_is_("Bad Request")
    assert success, message


@allure_annotations(
    title="Valid id",
    story="Delete",
    description='This test checks deleting a meme object with valid id in request',
    severity=allure.severity_level.CRITICAL,
    tag='Positive'
)
@pytest.mark.critical
def test_delete_meme_object(delete_meme_endpoint, meme_id_without_del, auth_token: str) -> None:
    delete_meme_endpoint.delete_meme_object(meme_id_without_del, auth_token)
    success, message = delete_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = delete_meme_endpoint.check_response_message_is_("successfully deleted")
    assert success, message


@allure_annotations(
    title="Without authorization",
    story="Delete",
    description='This test checks deleting a meme object without authorization',
    severity=allure.severity_level.CRITICAL,
)
@pytest.mark.critical
def test_delete_meme_object_without_authorization(delete_meme_endpoint, meme_id, auth_token: str) -> None:
    delete_meme_endpoint.delete_meme_object(meme_id, 'invalid_token')
    success, message = delete_meme_endpoint.check_status_code_is_(401)
    assert success, message
    success, message = delete_meme_endpoint.check_response_message_is_("Unauthorized")
    assert success, message


@allure_annotations(
    title="Invalid id",
    story="Delete",
    description='This test checks deleting a meme object with invalid id in request',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.critical
def test_delete_meme_object_with_invalid_id(delete_meme_endpoint, meme_id, auth_token: str) -> None:
    delete_meme_endpoint.delete_meme_object(0, auth_token)
    success, message = delete_meme_endpoint.check_status_code_is_(404)
    assert success, message
    success, message = delete_meme_endpoint.check_response_message_is_("Not Found")
    assert success, message
