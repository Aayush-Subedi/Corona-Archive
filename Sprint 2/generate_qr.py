def generate_qr(id):
    img = qrcode.make(id)
    filename = f"qr{id}.png"
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))