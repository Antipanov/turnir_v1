from ..extensions import db


class ParticipantsDB(db.Model):
    participant_id = db.Column(db.Integer, primary_key=True)
    participant_first_name = db.Column(db.String)
    participant_last_name = db.Column(db.String)
    activity_status = db.Column(db.Integer, default=1)
    red_fighter = db.relationship('FightsDB', backref='red_fighter', foreign_keys="[FightsDB.red_fighter_id]")
    blue_fighter = db.relationship('FightsDB', backref='blue_fighter', foreign_keys="[FightsDB.blue_fighter_id]")


class FightsDB(db.Model):
    fight_id = db.Column(db.Integer, primary_key=True)
    round_number = db.Column(db.Integer)
    red_fighter_id = db.Column(db.Integer, db.ForeignKey('participantsDB.participant_id'))
    blue_fighter_id = db.Column(db.Integer, db.ForeignKey('participantsDB.participant_id'))
    fight_winner_id = db.Column(db.Integer, default=0)
