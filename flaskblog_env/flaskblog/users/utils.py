def save_picture(form_picture):
    random_hex = secrets.token_hex(8)  # generate hex token of 8 bytes
    _, f_ext = os.path.splitext(form_picture.filename)  # split filename and extension. Dropping filename using '_'
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn) # app.root_path gives path upto package -> flaskblog
    output_size = (125, 125)
    i = Image.open(form_picture)  # opening image using pillow
    i.thumbnail(output_size)    # resize image to output size
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply igonre this email and no change will be made.
'''
    mail.send(msg)