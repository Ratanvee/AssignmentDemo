import requests
import json

def test_api():
    # Login to get token
    login_url = 'http://localhost:8000/api/login/'
    login_data = {
        'username': 'testuser',
        'password': '1234'
    }
    
    try:
        # Get authentication token
        response = requests.post(login_url, json=login_data)
        token_data = response.json()
        print("\nLogin Response:")
        print(json.dumps(token_data, indent=2))
        
        if 'access_token' in token_data:
            # Get jobs list using token
            jobs_url = 'http://localhost:8000/api/jobs/'
            headers = {
                'Authorization': f'Bearer {token_data["access_token"]}'
            }
            
            jobs_response = requests.get(jobs_url, headers=headers)
            jobs_data = jobs_response.json()
            print("\nJobs Response:")
            print(json.dumps(jobs_data, indent=2))
    
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()