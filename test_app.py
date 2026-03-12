from app import app

def test_get_bugs():
    tester = app.test_client()
    response = tester.get("/bugs")
    assert response.status_code == 200

def test_add_bug():
    tester = app.test_client()
    response = tester.post("/bugs", json={"title": "Test bug"})
    assert response.status_code == 200