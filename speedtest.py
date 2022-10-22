import speedtest

test = speedtest.Speedtest()

down_speed = test.download()
up_speed = test.upload()

print("Szybkość pobierania:", down_speed)
print("Szybkość wysyłania:", up_speed)
