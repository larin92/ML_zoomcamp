from lambda_function import predict


img_url = "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"

result = predict(img_url)

print(result)
