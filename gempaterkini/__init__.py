def ekstraksi_data():
    import requests
    from bs4 import BeautifulSoup
    try:
        content = requests.get("https://www.bmkg.go.id")
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('span', {'class':'waktu'})
        title = title.text.split(', ')
        tanggal=title[0]
        waktu=title[1]
        print('Tanggal:', tanggal)
        print('Waktu:', waktu)

        magnetudo = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        magnetudo = magnetudo.findChildren('li')
        i = 0
        for res in magnetudo:
            #print(i, res)
            if i == 1:
                magnetudo = res.text
                print('Magnetudo:', magnetudo)

            elif i ==2:
                kedalaman = res.text
                print('Kedalaman:', kedalaman)
            elif i==3:
                koordinat = res.text.split(' - ')
                print('LS: ', koordinat[0])
                print('BT: ', koordinat[1])
            i = i + 1


    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

