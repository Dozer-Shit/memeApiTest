import allure
import pytest

from meme_api_tests.tests.data import payloads

from meme_api_tests.client import allure_annotations


@allure_annotations(
    title="Authorization test",
    story="POST",
    description='This test checks creating a token',
    severity=allure.severity_level.BLOCKER,
    tag='!!!'
)
@pytest.mark.blocker
def test_get_auth_token(post_authorize_endpoint) -> None:
    post_authorize_endpoint.get_token(payloads.get_token)
    success, message = post_authorize_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = post_authorize_endpoint.check_response_name_is_(payloads.get_token['name'])
    assert success, message


@allure_annotations(
    title="Live token test",
    story="POST",
    description='This test checks token relevance',
    severity=allure.severity_level.MINOR,
)
@pytest.mark.minor
def test_check_auth_token(get_check_token_endpoint, auth_token: str) -> None:
    get_check_token_endpoint.check_token_is_valid(auth_token)
    success, message = get_check_token_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = get_check_token_endpoint.check_response_message_is_("Token is alive")
    assert success, message


@allure_annotations(
    title="Adding a meme object test",
    story="POST",
    description='This test checks adding a meme object',
    severity=allure.severity_level.CRITICAL,
    tag='!!!'
)
@pytest.mark.critical
def test_create_meme_object(post_meme_endpoint, delete_meme, request, auth_token: str) -> None:
    request.node.meme_id = post_meme_endpoint.create_meme_object(payloads.create_meme, auth_token)
    success, message = post_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = post_meme_endpoint.check_response_url_is_(payloads.create_meme['url'])
    assert success, message


@allure_annotations(
    title="Get meme object test",
    story="GET",
    description='This test checks getting a meme object',
    severity=allure.severity_level.MINOR
)
@pytest.mark.minor
def test_get_meme_object(get_meme_endpoint, meme_id: int, auth_token: str) -> None:
    get_meme_endpoint.get_meme(meme_id, auth_token)
    success, message = get_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = get_meme_endpoint.check_response_id_is_(meme_id)
    assert success, message


@allure_annotations(
    title="Get all meme objects test",
    story="GET",
    description='This test checks getting all meme objects',
    severity=allure.severity_level.MINOR
)
@pytest.mark.minor
def test_get_all_meme_objects(get_all_meme_endpoint, auth_token: str) -> None:
    get_all_meme_endpoint.get_all_meme(auth_token)
    success, message = get_all_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = get_all_meme_endpoint.check_response_is_not_empty()
    assert success, message


@allure_annotations(
    title="Update meme object test",
    story="PUT",
    description='This test checks updating a meme object',
)
@pytest.mark.parametrize("request_data", payloads.update_payloads(), ids=payloads.payload_ids)
def test_update_object(update_meme_endpoint, request_data: dict, meme_id: int, auth_token: str) -> None:
    request_data["id"] = meme_id
    update_meme_endpoint.update_meme_object(request_data, meme_id, auth_token)
    success, message = update_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = update_meme_endpoint.check_response_text_is_(request_data['text'])
    assert success, message
    success, message = update_meme_endpoint.check_response_title_is_(request_data['info']['title'])
    assert success, message


@allure_annotations(
    title="Delete meme object test",
    story="DELETE",
    description='This test checks deleting a meme object',
    tag='!!!',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.critical
def test_delete_meme_object(delete_meme_endpoint, meme_id_without_del, auth_token: str) -> None:
    delete_meme_endpoint.delete_meme_object(meme_id_without_del, auth_token)
    success, message = delete_meme_endpoint.check_status_code_is_(200)
    assert success, message
    success, message = delete_meme_endpoint.check_response_message_is_("successfully deleted")
    assert success, message
