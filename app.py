def create_app():
    from skrilla.Blog.blog_routes import blogs
    app.register_blueprint(blogs)
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    @click.command(name='create_admin')   
    @with_appcontext
    def create_admin():
        admin=User(email="admin_email_address",password="admin_password")
        admin.password = generate_password_hash(admin.password,'sha256',salt_length=12)
        db.session.add(admin)
        db.session.commit()

    app.cli.add_command(create_admin)
    app.config['JWT_SECRET_KEY']='YOUR_SECRET_KEY'
    jwt=JWTManager(app)
    
    db.init_app(app)

    return app
