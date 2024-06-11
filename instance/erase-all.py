import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Créer une connexion à la base de données
engine = create_engine('sqlite:///hotels.db')

# Créer une session
Session = sessionmaker(bind=engine)
session = Session()

# Récupérer les métadonnées des tables
metadata = MetaData()

# Lier le moteur (engine) à ces métadonnées
metadata.reflect(bind=engine)

# Parcourir toutes les tables dans la base de données et les vider
for table in reversed(metadata.sorted_tables):
    session.execute(table.delete())

# Valider les suppressions
session.commit()

# Fermer la session
session.close()
