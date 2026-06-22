import qrcode
upi_id = input('Enter your ID')

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%Name&mc=1234'



phonepayqrcode= qrcode.make(phonepay_url)
googlepayqrcode=qrcode.make(googlepay_url)
paytmqrcode=qrcode.make(paytm_url)

phonepayqrcode.save('phonepayqrcode.png')
googlepayqrcode.save('googlepayqrcode.png')
paytmqrcode.save('paytmqrcode.png')

phonepayqrcode.show()
googlepayqrcode.show()
phonepayqrcode.show()
