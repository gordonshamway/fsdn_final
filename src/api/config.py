import os


class DevConfig(object):
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    FLASK_SECRET = SECRET_KEY
    DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
    DB_NAME = 'corona2'
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_URI = os.getenv('DB_URI', 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_NAME))
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN', 'sbu47533.eu.auth0.com')
    ALGORITHMS = os.getenv['ALGORITHMS', ['RS256']]
    API_AUDIENCE = os.getenv('API_AUDIENCE', 'http://localhost:5000')
    ADMIN_TOKEN = os.getenv('ADMIN_TOKEN', (
        'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNK'
        'enZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWI'
        'iOiJhdXRoMHw2MDBkNGRiNzhlNWY1MzAwNmE4MjQ1Y2YiLCJhdWQiOiJodHRwOi8vbG9'
        'jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk0MzksImV4cCI6MTYxMTYwNjYzOSwiYXp'
        'wIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInB'
        'lcm1pc3Npb25zIjpbImRlbGV0ZTpyZXN0YXVyYW50IiwiZGVsZXRlOnJlc3RhdXJhbnQ'
        'tdGFibGUiLCJnZXQ6Z3Vlc3QtZGV0YWlscyIsImdldDpndWVzdC1ub3RpZmljYXRpb25'
        'zIiwiZ2V0Omd1ZXN0cyIsImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV'
        '0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOmd1ZXN0LWRldGFpbHM'
        'iLCJwYXRjaDpyZXN0YXVyYW50LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l'
        '0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQ'
        'tdGFibGUiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.sUJbxpPFm0tQV5z5-Kc9gi'
        'cFxXwU5AYkKtE6VZdFpL8r5Ftqu1wGVh_tX0xNc8AqQOQGMS5CwGpQuEXO7_ptPt1xKz'
        'ubydR8PXRtN2tTeBIeAvz-PH_vofy_2DMli84tBGdLOYNfOVmuefAHlo2sgVQy9qmobR'
        'rKHYpBMLV16Eppd0mM4ri34jKUAi6L7PZkz-7oN9r-SghpFOp0qeyv3Sa0dv-Gmi3W47'
        'MlLqveDcVx-pnLUI6890ZXgdFenyQRif8ECrtuuBhL3NhPFfsL2n1kI00jpLZg3C1UtN'
        'jnDzJS75DMmuhBFS7MOChJGaRiyPhAh_5F7m_wgeVw-hku0Q'))
    RESTAURANT_MANAGER_TOKEN = os.getenv('RESTAURANT_MANAGER_TOKEN', (
        'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNK'
        'enZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWI'
        'iOiJhdXRoMHw2MDBkNGUzZDAzMGI4ZjAwNmE1MTQzODIiLCJhdWQiOiJodHRwOi8vbG9'
        'jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2MDUsImV4cCI6MTYxMTYwNjgwNSwiYXp'
        'wIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInB'
        'lcm1pc3Npb25zIjpbImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWl'
        'scyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOnJlc3RhdXJhbnQtZGV0YWl'
        'scyIsInBvc3Q6cmVzdGF1cmFudCIsInBvc3Q6cmVzdGF1cmFudC10YWJsZSJdfQ.OlSv'
        'q3GVHNaab6gWDl_CNfb7p-UCwdqr5Ut4mM-ZX5sU1Yt0WrWiXDLgd6fMYOSlEtsDlybm'
        'g-M-XS-B9BVbrK1yrW8FESysFM9_Zq-Q386GzBsPUWCqVG7QGoruHa4kvkJhMeytbRLQ'
        'rk3lV_F1ngkyjZ1CvbgD0Z2GokKnUlpT3GhD4j1oO2rwUoFYQ9lpvZngJe_dsMLVrMxx'
        'DS8jMhYJiapKL4B-57Ddojb6oT58AE_IRe3KGruSd8GFS309HMV7w_eB7g-7PYUVA0xN'
        'jbMC4lSy0MOFoBS3GjGfBjdQkNe5ew9YcFi_gqoS9WpDgqmxC8KMuKyaYF8KnwN4fw'))
    GUEST_TOKEN = os.getenv('GUEST_TOKEN', (
        'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNK'
        'enZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWI'
        'iOiJhdXRoMHw2MDBkNGU1ZDhlNWY1MzAwNmE4MjQ2MDEiLCJhdWQiOiJodHRwOi8vbG9'
        'jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2NTAsImV4cCI6MTYxMTYwNjg1MCwiYXp'
        'wIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInB'
        'lcm1pc3Npb25zIjpbImdldDpndWVzdC1kZXRhaWxzIiwiZ2V0Omd1ZXN0LW5vdGlmaWN'
        'hdGlvbnMiLCJnZXQ6cmVzdGF1cmFudCIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXR'
        'jaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQ'
        'tdmlzaXRzIl19.dl7YTAP6jxr5PTOeVrlOzuDDhne87HcpJhYimxeCo6g12XFJ8qxiQJ'
        'c-JuDlyUMJol5WftGTFkQJ6syd8PNZ8yD9Zg-Nct_PgaNBKBEz-UPvvr5wRWYNdfFc1q'
        'Roen6mFSCwq1vXrL7azq0adaitLABzBQYfnruG2aX_p222QUU1ZnipgmpmDu4dtwiZyp'
        'qAtheWRtH1icvGiFQ6Eg7WXe4KjQrOvSQ_1MQAnU61YniLUT6juv2dn0sGa2fDTeiQwH'
        'Ja2Avjw8lpr_7-x7mnO5xtM3QAQRrx9kZFj0aZ7MUWeFSEX6LNKV0ZwfY5yviyg3AkrY'
        '8DJiB4TDenQBrh8Q'))


class TestConfig(DevConfig):
    DB_NAME = 'corona_test'
    DB_USER = os.getenv('TEST_DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('TEST_DB_PASSWORD', 'postgres')
    DB_HOST = os.getenv('TEST_DB_HOST', 'localhost:5432')
    DB_URI = os.getenv(
        'DB_URI', 'postgresql+psycopg2://{}:{}@{}/{}'.format(
            DB_USER,
            DB_PASSWORD,
            DB_HOST,
            DB_NAME))
    SQLALCHEMY_DATABASE_URI = DB_URI
    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN', 'sbu47533.eu.auth0.com')
    ALGORITHMS = os.getenv['ALGORITHMS', ['RS256']]
    API_AUDIENCE = os.getenv('API_AUDIENCE', 'http://localhost:5000')
    ADMIN_TOKEN = os.getenv('ADMIN_TOKEN', (
        'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNK'
        'enZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWI'
        'iOiJhdXRoMHw2MDBkNGRiNzhlNWY1MzAwNmE4MjQ1Y2YiLCJhdWQiOiJodHRwOi8vbG9'
        'jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk0MzksImV4cCI6MTYxMTYwNjYzOSwiYXp'
        'wIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInB'
        'lcm1pc3Npb25zIjpbImRlbGV0ZTpyZXN0YXVyYW50IiwiZGVsZXRlOnJlc3RhdXJhbnQ'
        'tdGFibGUiLCJnZXQ6Z3Vlc3QtZGV0YWlscyIsImdldDpndWVzdC1ub3RpZmljYXRpb25'
        'zIiwiZ2V0Omd1ZXN0cyIsImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV'
        '0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOmd1ZXN0LWRldGFpbHM'
        'iLCJwYXRjaDpyZXN0YXVyYW50LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l'
        '0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQ'
        'tdGFibGUiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.sUJbxpPFm0tQV5z5-Kc9gi'
        'cFxXwU5AYkKtE6VZdFpL8r5Ftqu1wGVh_tX0xNc8AqQOQGMS5CwGpQuEXO7_ptPt1xKz'
        'ubydR8PXRtN2tTeBIeAvz-PH_vofy_2DMli84tBGdLOYNfOVmuefAHlo2sgVQy9qmobR'
        'rKHYpBMLV16Eppd0mM4ri34jKUAi6L7PZkz-7oN9r-SghpFOp0qeyv3Sa0dv-Gmi3W47'
        'MlLqveDcVx-pnLUI6890ZXgdFenyQRif8ECrtuuBhL3NhPFfsL2n1kI00jpLZg3C1UtN'
        'jnDzJS75DMmuhBFS7MOChJGaRiyPhAh_5F7m_wgeVw-hku0Q'))
    RESTAURANT_MANAGER_TOKEN = os.getenv('RESTAURANT_MANAGER_TOKEN', (
        'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNK'
        'enZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWI'
        'iOiJhdXRoMHw2MDBkNGUzZDAzMGI4ZjAwNmE1MTQzODIiLCJhdWQiOiJodHRwOi8vbG9'
        'jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2MDUsImV4cCI6MTYxMTYwNjgwNSwiYXp'
        'wIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInB'
        'lcm1pc3Npb25zIjpbImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWl'
        'scyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOnJlc3RhdXJhbnQtZGV0YWl'
        'scyIsInBvc3Q6cmVzdGF1cmFudCIsInBvc3Q6cmVzdGF1cmFudC10YWJsZSJdfQ.OlSv'
        'q3GVHNaab6gWDl_CNfb7p-UCwdqr5Ut4mM-ZX5sU1Yt0WrWiXDLgd6fMYOSlEtsDlybm'
        'g-M-XS-B9BVbrK1yrW8FESysFM9_Zq-Q386GzBsPUWCqVG7QGoruHa4kvkJhMeytbRLQ'
        'rk3lV_F1ngkyjZ1CvbgD0Z2GokKnUlpT3GhD4j1oO2rwUoFYQ9lpvZngJe_dsMLVrMxx'
        'DS8jMhYJiapKL4B-57Ddojb6oT58AE_IRe3KGruSd8GFS309HMV7w_eB7g-7PYUVA0xN'
        'jbMC4lSy0MOFoBS3GjGfBjdQkNe5ew9YcFi_gqoS9WpDgqmxC8KMuKyaYF8KnwN4fw'))
    GUEST_TOKEN = os.getenv('GUEST_TOKEN', (
        'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNK'
        'enZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWI'
        'iOiJhdXRoMHw2MDBkNGU1ZDhlNWY1MzAwNmE4MjQ2MDEiLCJhdWQiOiJodHRwOi8vbG9'
        'jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2NTAsImV4cCI6MTYxMTYwNjg1MCwiYXp'
        'wIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInB'
        'lcm1pc3Npb25zIjpbImdldDpndWVzdC1kZXRhaWxzIiwiZ2V0Omd1ZXN0LW5vdGlmaWN'
        'hdGlvbnMiLCJnZXQ6cmVzdGF1cmFudCIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXR'
        'jaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQ'
        'tdmlzaXRzIl19.dl7YTAP6jxr5PTOeVrlOzuDDhne87HcpJhYimxeCo6g12XFJ8qxiQJ'
        'c-JuDlyUMJol5WftGTFkQJ6syd8PNZ8yD9Zg-Nct_PgaNBKBEz-UPvvr5wRWYNdfFc1q'
        'Roen6mFSCwq1vXrL7azq0adaitLABzBQYfnruG2aX_p222QUU1ZnipgmpmDu4dtwiZyp'
        'qAtheWRtH1icvGiFQ6Eg7WXe4KjQrOvSQ_1MQAnU61YniLUT6juv2dn0sGa2fDTeiQwH'
        'Ja2Avjw8lpr_7-x7mnO5xtM3QAQRrx9kZFj0aZ7MUWeFSEX6LNKV0ZwfY5yviyg3AkrY'
        '8DJiB4TDenQBrh8Q'))
