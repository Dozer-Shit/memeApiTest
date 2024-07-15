import pytest

from meme_api_tests.tests.data import payloads

from meme_api_tests.utils.client import AUTHORIZATION_TOKEN, save_token

from meme_api_tests.endpoints.get_check_token import GetCheckToken
from meme_api_tests.endpoints.put_upd_meme import PutUpdMeme
from meme_api_tests.endpoints.get_single_meme import GetMeme
from meme_api_tests.endpoints.get_all_meme import GetAllMeme
from meme_api_tests.endpoints.post_add_meme import PostAddMeme
from meme_api_tests.endpoints.post_authorize import PostAuthorize
from meme_api_tests.endpoints.delete_meme import DeleteMeme


@pytest.fixture(scope='session')
def auth_token(post_authorize_endpoint: PostAuthorize, get_check_token_endpoint: GetCheckToken) -> str:
    token = AUTHORIZATION_TOKEN
    if not token:
        token = post_authorize_endpoint.get_token(payloads.get_token)
        save_token(token)

    get_check_token_endpoint.check_token_is_valid(token)
    try:
        get_check_token_endpoint.check_response_message_is_("Token is alive")
    except AssertionError:
        token = post_authorize_endpoint.get_token(payloads.get_token)
        save_token(token)

    return token


@pytest.fixture
def meme_id(post_meme_endpoint: PostAddMeme, delete_meme_endpoint: DeleteMeme, auth_token: str) -> int:
    payload = payloads.create_meme
    meme_id = post_meme_endpoint.create_meme_object(payload, auth_token)
    yield meme_id
    delete_meme_endpoint.delete_meme_object(meme_id, auth_token)


@pytest.fixture
def meme_id_without_del(post_meme_endpoint: PostAddMeme, auth_token: str) -> int:
    payload = payloads.create_meme
    meme_id = post_meme_endpoint.create_meme_object(payload, auth_token)
    return meme_id


@pytest.fixture
def delete_meme(request: pytest.FixtureRequest, delete_meme_endpoint: 'DeleteMeme', auth_token: str, meme_id: int):
    yield
    meme_id = request.node.meme_id
    delete_meme_endpoint.delete_meme_object(meme_id, auth_token)


@pytest.fixture(scope='session')
def post_authorize_endpoint() -> PostAuthorize:
    return PostAuthorize()


@pytest.fixture(scope='session')
def get_check_token_endpoint() -> GetCheckToken:
    return GetCheckToken()


@pytest.fixture
def get_meme_endpoint() -> GetMeme:
    return GetMeme()


@pytest.fixture
def get_all_meme_endpoint() -> GetAllMeme:
    return GetAllMeme()


@pytest.fixture
def post_meme_endpoint() -> PostAddMeme:
    return PostAddMeme()


@pytest.fixture
def update_meme_endpoint() -> PutUpdMeme:
    return PutUpdMeme()


@pytest.fixture
def delete_meme_endpoint() -> DeleteMeme:
    return DeleteMeme()
