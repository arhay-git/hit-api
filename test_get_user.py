import requests


headers = {
    "Content-Type": "application/json",
    "x-api-key": "reqres_e2f07874d8a140329ddf0b1137dfbd27"
}

# @pytest.mark.parametrize('page', [1, 2, 3])
# def test_users(page):
#     response_get = requests.get(f'https://reqres.in/api/users?page={page}', headers=headers)
def test_users():
    response_get = requests.get('https://reqres.in/api/users?page=2', headers=headers)
    json_response = response_get.json()
    
    assert response_get.status_code == 200
    