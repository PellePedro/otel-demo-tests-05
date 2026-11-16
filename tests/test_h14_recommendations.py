import json  # noqa: F401


def test_h14_0puk6v6ev0_nzd_0001(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_php_0002(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_pln_0003(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_ron_0004(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_rub_0005(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_sek_0006(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_sgd_0007(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_thb_0008(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_try_0009(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_usd_0010(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_zar_0011(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_aud_0012(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_bgn_0013(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_brl_0014(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_cad_0015(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_chf_0016(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_cny_0017(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_czk_0018(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_dkk_0019(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_eur_0020(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_gbp_0021(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_hkd_0022(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_hrk_0023(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_huf_0024(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_idr_0025(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]
