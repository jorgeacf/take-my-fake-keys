import os
import random
import string

def generate_fake_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits + '/=+_-', k=length))

os.makedirs('honeypot_files', exist_ok=True)
os.chdir('honeypot_files')

for path in ['/.e5498', '/.env', '/.env.backup', '/.env.bak', '/.env.dev', '/.env.development', '/.env.local', '/.env.old', '/.env.prod', '/.env.production', '/.env.save', '/.env.staging', '/.env.swp', '/.env.test', '/.env.tmp', '/.env.vault', '/.env~', '/.git/config', '/.git/logs/HEAD', '/.secrets', '/.streamlit/secrets.toml', '/_next/static/chunks/app.js', '/_next/static/chunks/main.js', '/actuator/configprops', '/actuator/env', '/api/.env', '/api/config', '/api/env', '/api/settings', '/app.bundle.js', '/app.js', '/app/.env', '/application-dev.properties', '/application-prod.properties', '/application.properties', '/application.yaml', '/application.yml', '/appsettings.Development.json', '/appsettings.Production.json', '/appsettings.json', '/assets/app.js', '/assets/index.js', '/backend/.env', '/backup/.env', '/backups/.env', '/build/static/js/main.js', '/bundle.js', '/chunk.js', '/client/.env', '/conf/settings.json', '/config.js', '/config.json', '/config.py', '/config.toml', '/config.yaml', '/config.yml', '/config/.env', '/config/app.php', '/config/default.json', '/config/development.json', '/config/local.json', '/config/master.key', '/config/production.json', '/config/secrets.yml', '/credentials.json', '/data/config.json', '/dist/app.js', '/dist/bundle.js', '/dist/main.js', '/docker-compose.dev.yml', '/docker-compose.override.yml', '/docker-compose.prod.yml', '/docker-compose.yaml', '/docker-compose.yml', '/ecosystem.config.js', '/env', '/env.js', '/env.json', '/frontend/.env', '/home/ec2-user/.aws/credentials', '/home/node/.aws/credentials', '/home/ubuntu/.aws/credentials', '/index.js', '/js/app.js', '/js/main.js', '/laravel/.env', '/main.bundle.js', '/main.js', '/old/.env', '/private/.env', '/public/.env', '/root/.aws/credentials', '/root/.streamlit/secrets.toml', '/secrets.json', '/secrets.py', '/secrets.yaml', '/secrets.yml', '/server.js', '/server/.env', '/serverless.yaml', '/serverless.yml', '/settings.js', '/settings.json', '/settings.py', '/src/.env', '/static/js/app.js', '/static/js/bundle.js', '/static/js/main.js', '/storage/framework/.env', '/temp/.env', '/terraform.tfstate', '/terraform.tfvars', '/tmp/.env', '/var/.env', '/vendor.js', '/web/.env', '/wp-config.php.bak', '/wp-config.php.old', '/wp-config.php.save', '/wp-config.php.txt', '/wp-config.php~']:
    full_path = path.lstrip('/')
    dir_name = os.path.dirname(full_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    file_name = os.path.basename(full_path)
    ext = os.path.splitext(file_name)[1].lower()

    if 'env' in file_name.lower() or ext in ['.properties', '.swp', '', '.bak', '.old', '.save', '.txt', '~', '.vault', '.secrets'] or 'configprops' in file_name.lower() or 'env' in file_name.lower() or 'config' in file_name.lower() or 'settings' in file_name.lower():
        content = f"""
DB_HOST=localhost
DB_PORT=3306
DB_NAME=root
DB_USER=fakeuser
DB_PASSWORD=7Bl9pky9NW_sWV30rebd
API_KEY=7nXprU1C_jZDx-ARlK0sJsXIKiO51W39
SECRET_KEY=sPAuIKkjDVuJXhiGB2t3d-Q8y0=a2/H5iq580UCQq7VnJg4a=n
AWS_ACCESS_KEY_ID=AKIASJ9J+yq+1TUl79zI
AWS_SECRET_ACCESS_KEY=rlFuGLAD+7YLDYph25GatOPgk2lXP8_gTBaLyIpF
OPENAI_API_KEY=sk-q_PhE+wgFd49IJGgU3vkIJaz4jAE0HpXOll2I+x3g3_7+q-L
STRIPE_SECRET_KEY=sk_test_eLdtj/YSp_DQJEis1imeCwaYX0RsKwUSeR_=uHaF
""".strip()
    elif ext == '.json':
        content = '{\n  "db_password": "mX=2Y8Md8Qd2ebFX3lCm",\n  "api_key": "M0T=B+Su3xzXBmo=EWKOaUCpf1k=a8Oe",\n  "secret": "mo8M48OJh9WOQFbV/Br/osp_GtQcZGZftbvybQo78t0hCeb6u6",\n  "aws_access_key": "AKIA+2ePaa4F7JKH7MmJ",\n  "aws_secret_key": "sM14mszfjRHUf5ayrn7AL5eObj9MVC1r1DNM8c-l"\n}'
    elif ext in ['.yml', '.yaml']:
        content = 'db:\n  host: localhost\n  port: 3306\n  name: fakedb\n  user: fakeuser\n  password: su0YZYl04zzHDTUWNQo0\napi_key: i=Fuym60Zv7IWqbjIk2htGhg9w+gWJQD\nsecret_key: bBd1jEI3xUn2BeBhx7yGzWZ/MkEltX3OSJ1n4BrVI-K-tF3tRP\naws:\n  access_key_id: AKIAbUo0vVr=+du+reNL\n  secret_access_key: rrACPNwJpUi/UHTht/F4HuAnPNzMIUQobMrUj6+g\n'
    elif ext == '.js':
        content = "const config = {\n  DB_PASSWORD: 'h=odNj2uV_CDifc2fJA-',\n  API_KEY: 'D3_W0T7+7x7Ph9NCkaQO23z0LP=8wFWu',\n  SECRET: 'Ik5q7_EGqpff7bPnMZERhwLv0ZtZUr-=EGSF_0n+L9dYjw/FKh'\n};\n"
    elif ext == '.py':
        content = "DB_PASSWORD = 'lzE2-L6lJWdBDud0zJJ8'\nAPI_KEY = '/_RXYq-XdBsgFCd0cQACzaBsfrZ34J7s'\nSECRET_KEY = 'goy4bdlPLPrIPH8QDIIiRN+j-Qs-OnI06OQn+Xlj_jnopQf6XV'\n"
    elif ext == '.php':
        content = "<?php\ndefine('DB_PASSWORD', 'jtJCwgWnOtYNRoykc-5S');\ndefine('API_KEY', 'aGsRZQBrMSGWT19JzPzrRn5cuEfEcRgI');\ndefine('SECRET_KEY', 'rXlsCJg0V=m=ajREkMWlDeJjsIsQ6NxHGmszbg7ILMq5TpY/lh');\n?>\n"
    elif ext == '.toml':
        content = '[database]\nhost = "localhost"\nport = 3306\nname = "fakedb"\nuser = "fakeuser"\npassword = "EbJ9wm_RdfyRZQxK6l0f"\n\napi_key = "T9Z+paSDoxBP3p-J9D0l9utH9XA0-dSR"\nsecret_key = "cug0yIvxRT=QJ6KIwW3FjjvOg/-T-Vnlr8tzdyghIv8NFgPy6-"\n'
    elif file_name == 'config' and dir_name.endswith('.git'):
        content = '[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = true\n[remote "origin"]\n\turl = https://github.com/fake/repo.git\n\tfetch = +refs/heads/*:refs/remotes/origin/*\n[branch "main"]\n\tremote = origin\n\tmerge = refs/heads/main\n'
    elif 'credentials' in file_name.lower():
        content = '[default]\naws_access_key_id = AKIAjWhdhJYUDlD+hxZa\naws_secret_access_key = hx4iFtBJ8OfrsXrCE3U2V7li9vTn9x+q-1rhR/ad\n'
    elif 'master.key' in file_name.lower():
        content = 'aqM-8UV4aEU+P/K9_ewtqC0RFDz7-8zZURjBuxuA0XA0Z1tBl_yoOfmAY+iLoH4/'
    elif 'tfvars' in file_name.lower() or 'tfstate' in file_name.lower():
        content = 'aws_access_key = "AKIAs2lkE=XLKlOuBim+"\naws_secret_key = "4YjFDSDOO800SJkSGbk2vjQOJcfpRoTV/Ps=O+qo"\n'
    elif 'head' in file_name.lower():
        content = 'fake git log content'
    else:
        content = f"""
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fakedb
DB_USER=fakeuser
DB_PASSWORD=7Bl9pky9NW_sWV30rebd
API_KEY=7nXprU1C_jZDx-ARlK0sJsXIKiO51W39
SECRET_KEY=sPAuIKkjDVuJXhiGB2t3d-Q8y0=a2/H5iq580UCQq7VnJg4a=n
AWS_ACCESS_KEY_ID=AKIASJ9J+yq+1TUl79zI
AWS_SECRET_ACCESS_KEY=rlFuGLAD+7YLDYph25GatOPgk2lXP8_gTBaLyIpF
OPENAI_API_KEY=sk-q_PhE+wgFd49IJGgU3vkIJaz4jAE0HpXOll2I+x3g3_7+q-L
STRIPE_SECRET_KEY=sk_test_eLdtj/YSp_DQJEis1imeCwaYX0RsKwUSeR_=uHaF
""".strip()

    with open(full_path, 'w') as f:
        f.write(content)