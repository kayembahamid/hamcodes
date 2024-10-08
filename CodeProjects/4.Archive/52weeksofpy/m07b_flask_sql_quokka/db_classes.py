from extensions import db


class Device(db.Model):

    __tablename__ = "device"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text, unique=True, nullable=False)
    fqdn = db.Column(db.Text)
    serial = db.Column(db.Text)
    ip_address = db.Column(db.Text)
    mac_address = db.Column(db.Text)
    vendor = db.Column(db.Text)
    model = db.Column(db.Text)
    os = db.Column(db.Text)
    os_version = db.Column(db.Text)
    transport = db.Column(db.Text)

    availability = db.Column(db.Boolean)
    response_time = db.Column(db.Integer)
    sla_availability = db.Column(db.Integer, default=0)
    sla_response_time = db.Column(db.Integer, default=99999)

    last_heard = db.Column(db.Text)

    ssh_port = db.Column(db.Integer)

    hostname = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __repr__(self):
        return f"Device:{self.name}"


class Host(db.Model):

    __tablename__ = "host"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.Text, nullable=False)
    ip_address = db.Column(db.Text, nullable=False)
    mac_address = db.Column(db.Text)

    availability = db.Column(db.Boolean)
    response_time = db.Column(db.Integer)

    last_heard = db.Column(db.Text)

    def __repr__(self):
        return f"Host: {self.hostname}"


class Service(db.Model):

    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text)
    target = db.Column(db.Text, nullable=False)
    data = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)


    availability = db.Column(db.Boolean)
    response_time = db.Column(db.Integer)
    sla_availability = db.Column(db.Integer, default=0)
    sla_response_time = db.Column(db.Integer, default=99999)

    last_heard = db.Column(db.Text)
    def __repr__(self):
        return f"Service: {self.name}"
