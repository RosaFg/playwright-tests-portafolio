def test_load_time_under_2s(page):
    page.goto("https://portafolio-rosafg.netlify.app/")
    timing = page.evaluate("performance.timing")
    load_time = timing["loadEventEnd"] - timing["navigationStart"]
    assert load_time < 2000, f"Carga lenta: {load_time}ms"
