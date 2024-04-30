import requests

def get_user_info(username, token):
    url = f"https://api.github.com/users/{username}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        print("Errore nell'interrogazione delle API di GitHub.")
        return None

def get_all_followers(username, token):
    followers_list = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/followers?page={page}&per_page=100"
        headers = {'Authorization': f'token {token}'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            followers = response.json()
            if not followers:
                break
            followers_list.extend(followers)
            page += 1
        else:
            print("Errore nell'interrogazione delle API di GitHub per i follower.")
            return None
    return followers_list

def get_all_following(username, token):
    following_list = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/following?page={page}&per_page=100"
        headers = {'Authorization': f'token {token}'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            following = response.json()
            if not following:
                break
            following_list.extend(following)
            page += 1
        else:
            print("Errore nell'interrogazione delle API di GitHub per i following.")
            return None
    return following_list

def get_user_repositories(username, token):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print("Errore nell'interrogazione delle API di GitHub per i repository.")
        return None

def get_repo_description(repo_name, username, token):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info.get('description', 'N/A')
    else:
        print(f"Errore nell'interrogazione delle API di GitHub per il repository {repo_name}.")
        return None

def main():
    username = input("Inserisci il nome utente di GitHub: ")
    token = input("Inserisci il tuo token personale GitHub: ")
    
    user_info = get_user_info(username, token)
    if user_info:
        print(f"Informazioni su {username}:")
        print(f"Nome utente: {user_info['login']}")
        print(f"Nome: {user_info['name']}")
        print(f"Email: {user_info.get('email', 'N/A')}")
        print(f"Numero di follower: {user_info['followers']}")
        print(f"Numero di following: {user_info['following']}")
        print(f"Location: {user_info['location']}")
        print(f"Bio: {user_info.get('bio', 'N/A')}")

        followers_list = get_all_followers(username, token)
        if followers_list:
            print("\nLista dei Follower:")
            for follower in followers_list:
                print(follower['login'])

        following_list = get_all_following(username, token)
        if following_list:
            print("\nLista dei Following:")
            for following in following_list:
                print(following['login'])

        repositories = get_user_repositories(username, token)
        if repositories:
            print("\nRepository:")
            for repo in repositories:
                description = get_repo_description(repo['name'], username, token)
                print(f"Nome: {repo['name']}")
                print(f"Descrizione: {description}")
        else:
            print("Impossibile recuperare i repository.")
    else:
        print("Impossibile recuperare le informazioni dell'utente.")

if __name__ == "__main__":
    main()
