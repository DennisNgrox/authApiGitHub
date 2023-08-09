from octokit import Octokit

user = input('Digite o nome do usuário: ')
response = Octokit(auth='token', token='<your_token>')

repo = response.repos.list_for_user(username=user)

for r in repo.json:
    print(r['name'])
