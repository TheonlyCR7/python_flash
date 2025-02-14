def test_full_auth_flow(client, db_session):
    # 注册
    client.post('/reg', json={...})

    # 登录
    login_res = client.post('/login', json={
        'username': 'test@example.com',
        'password': 'validPass123',
        'vcode': 'mocked_vcode'
    })

    assert 'session' in login_res.headers['Set-Cookie']
    assert login_res.json['data'] == '登录成功'

    # 访问个人中心
    profile_res = client.get('/personal')
    assert profile_res.status_code == 200