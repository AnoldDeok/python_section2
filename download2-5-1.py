from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
print(">>",urljoin(baseUrl, "b.html"))
print(">>",urljoin(baseUrl, "../index.html"))
print(">>",urljoin(baseUrl, "../css/a.css"))
