from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, City, Immobile, User, engine


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

User1 = User(name="Robot", email="robot@gmail.com")
session.add(User1)
session.commit()

city1 = City(name="Rio de Janeiro", user_id="1")

session.add(city1)
session.commit()

immobileDetails1 = Immobile(address="Rua Ituverava, 1033, Rio de Janeiro",
                            description="House",
                            squarefeet="1323 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="4 bathrooms",
                            city=city1,
                            user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(
    address="Rua Henrique de Novais, 155, Rio de Janeiro",
    description="Apartment",
    squarefeet="839 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="3 bathroom",
    city=city1,
    user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address="Rua Caruso, 19, Rio de Janeiro",
                            description="House",
                            squarefeet="4305 squarefeet",
                            bedrooms="7 bedrooms",
                            bathrooms="4 bathrooms",
                            city=city1,
                            user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(
    address="Rua Professor Gabiso, 135, Rio de Janeiro",
    description="House",
    squarefeet="4187 squarefeet",
    bedrooms="4 bedrooms",
    bathrooms="3 bathrooms",
    city=city1,
    user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Rua Franco Zampari, 111, Rio de Janeiro",
                            description="Apartment",
                            squarefeet="796 squarefeet",
                            bedrooms="2 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city1,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

city2 = City(name="Sao Paulo", user_id="1")

session.add(city2)
session.commit()

immobileDetails1 = Immobile(address="Rua Sao Joao Cabral, 48, Sao Paulo",
                            description="House",
                            squarefeet="1808 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city2,
                            user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address="Rua Camburiu, 413, Sao Paulo",
                            description="Apartment",
                            squarefeet="721 squarefeet",
                            bedrooms="2 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city2,
                            user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(
    address="Rua Dr. Joao Jorge Sabino, 270, Sao Paulo",
    description="House",
    squarefeet="1216 squarefeet",
    bedrooms="4 bedrooms",
    bathrooms="2 bathrooms",
    city=city2,
    user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(
    address="Avenida Escragnolle Doria, 322, Sao Paulo",
    description="House",
    squarefeet="1453 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="2 bathrooms",
    city=city2,
    user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Rua Jose Cola Grossi, Sao Paulo",
                            description="House",
                            squarefeet="3993 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="4 bathrooms",
                            city=city2,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

city3 = City(name="Belo Horizonte",
             user_id="1")

session.add(city3)
session.commit()

immobileDetails1 = Immobile(
    address="Rua Coronel Emilio Martins, 140, Belo Horizonte",
    description="House",
    squarefeet="2271 squarefeet",
    bedrooms="4 bedrooms",
    bathrooms="3 bathrooms",
    city=city3,
    user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address="Rua Purus, Belo Horizonte",
                            description="House",
                            squarefeet="624 squarefeet",
                            bedrooms="2 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city3,
                            user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(
    address="Rua Deputado Gregoriano Canedo, 698, Belo Horizonte",
    description="House",
    squarefeet="968 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="3 bathrooms",
    city=city3,
    user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(
    address="Rua Heitor Socrates Cardoso, 587, Belo Horizonte",
    description="House",
    squarefeet="1937 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="3 bathrooms",
    city=city3,
    user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(
    address="Rua Jaime Petiti da Silva, 196, Belo Horizonte",
    description="House",
    squarefeet="3875 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="3 bathrooms",
    city=city3,
    user_id="1")

session.add(immobileDetails5)
session.commit()

city4 = City(name="Porto Alegre",
             user_id="1")

session.add(city4)
session.commit()

immobileDetails1 = Immobile(address="Rua General Rondon, 123, Porto Alegre",
                            description="House",
                            squarefeet="3552 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city4,
                            user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(
    address="Rua Conselheiro Xavier da Costa, 2431, Porto Alegre",
    description="House",
    squarefeet="5920 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="5 bathrooms",
    city=city4,
    user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address="Rua Dona Augusta, 244, Porto Alegre",
                            description="House",
                            squarefeet="1399 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city4,
                            user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(
    address="Rua Pedro Carneiro Pereira, 65, Porto Alegre",
    description="House",
    squarefeet="3993 squarefeet",
    bedrooms="4 bedrooms",
    bathrooms="4 bathrooms",
    city=city4,
    user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(
    address="Avenida Vicente Monteggia, 586, Porto Alegre",
    description="House",
    squarefeet="3444 squarefeet",
    bedrooms="7 bedrooms",
    bathrooms="4 bathrooms",
    city=city4,
    user_id="1")

session.add(immobileDetails5)
session.commit()

city5 = City(name="Vitoria",
             user_id="1")

session.add(city5)
session.commit()

immobileDetails1 = Immobile(
    address="Avenida Desembargador Alfredo Cabral, 870, Vitoria",
    description="House",
    squarefeet="12916 squarefeet",
    bedrooms="4 bedrooms",
    bathrooms="6 bathrooms",
    city=city5,
    user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address="Rua Avenida Antonio Borges, 186, Vitoria",
                            description="House",
                            squarefeet="9343 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="5 bathrooms",
                            city=city5,
                            user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address="Rua Fortunato Abreu Gagno, Vitoria",
                            description="House",
                            squarefeet="2690 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city5,
                            user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address="Rua Manoel Gomes de Almeida, Vitoria",
                            description="House",
                            squarefeet="8880 squarefeet",
                            bedrooms="5 bedrooms",
                            bathrooms="4 bathrooms",
                            city=city5,
                            user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Rua General Camara, 96, Vitoria",
                            description="House",
                            squarefeet="2368 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city5,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

city6 = City(name="Curitiba",
             user_id="1")

session.add(city6)
session.commit()

immobileDetails1 = Immobile(
    address="Rua Capitao Tenente Maris de Barros, 313, Curitiba",
    description="Apartment",
    squarefeet="753 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="2 bathrooms",
    city=city6,
    user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address="Rua Rua Antonio Gasparin, 4911, Curitiba",
                            description="Apartment",
                            squarefeet="1140 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city6,
                            user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address="Avenida Rep. Argentina, 2524, Curitiba",
                            description="Apartment",
                            squarefeet="678 squarefeet",
                            bedrooms="2 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city6,
                            user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address="Rua Dona Alice Tibirica, 611, Curitiba",
                            description="Apartment",
                            squarefeet="1593 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="5 bathrooms",
                            city=city6,
                            user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Rua Gago Coutinho, 45, Curitiba",
                            description="Apartment",
                            squarefeet="1022 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city6,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

city7 = City(name="Florianopolis",
             user_id="1")

session.add(city7)
session.commit()

immobileDetails1 = Immobile(
    address="Servidao Belo Horizonte, 390, Florianopolis",
    description="House",
    squarefeet="645 squarefeet",
    bedrooms="2 bedrooms",
    bathrooms="1 bathrooms",
    city=city7,
    user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(
    address="Rua Manoel Pedro Teixeira, 1, Florianopolis",
    description="House",
    squarefeet="753 squarefeet",
    bedrooms="2 bedrooms",
    bathrooms="1 bathrooms",
    city=city7,
    user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(
    address="Servidao Sotero Jose de Farias, 429, Florianopolis",
    description="House",
    squarefeet="2152 squarefeet",
    bedrooms="3 bedrooms",
    bathrooms="2 bathrooms",
    city=city7,
    user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address="Joao Jose Adriano, 188, Florianopolis",
                            description="House",
                            squarefeet="2820 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="4 bathrooms",
                            city=city7,
                            user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Servidao Bons Amigos, 300, Florianopolis",
                            description="House",
                            squarefeet="1237 squarefeet",
                            bedrooms="2 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city7,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

city8 = City(name="Salvador",
             user_id="1")

session.add(city8)
session.commit()

immobileDetails1 = Immobile(address="Rua das Azaleias, 184, Salvador",
                            description="House",
                            squarefeet="4413 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="5 bathrooms",
                            city=city8,
                            user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address="Avenida Alphaville, 100, Salvador",
                            description="House",
                            squarefeet="3821 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="6 bathrooms",
                            city=city8,
                            user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address="Alameda das Samambaias, 620, Salvador",
                            description="House",
                            squarefeet="1345 squarefeet",
                            bedrooms="2 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city8,
                            user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address="Rua Ramalho Ortigao, 51, Salvador",
                            description="House",
                            squarefeet="4305 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="5 bathrooms",
                            city=city8,
                            user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Avenida Dorival Caymmi, 63, Salvador",
                            description="House",
                            squarefeet="914 squarefeet",
                            bedrooms="2 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city8,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

city9 = City(name="Gramado",
             user_id="1")

session.add(city9)
session.commit()

immobileDetails1 = Immobile(address="Rua Leopoldo Geier, 174, Gramado",
                            description="House",
                            squarefeet="1087 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city9,
                            user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address="Rua Joao Alfredo Schneider, 792, Gramado",
                            description="House",
                            squarefeet="3552 squarefeet",
                            bedrooms="6 bedrooms",
                            bathrooms="5 bathrooms",
                            city=city9,
                            user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address="Rua Nereu Ramos, 223, Gramado",
                            description="House",
                            squarefeet="1829 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="3 bathrooms",
                            city=city9,
                            user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address="Rua Nereu Ramos, 333, Gramado",
                            description="House",
                            squarefeet="2475 squarefeet",
                            bedrooms="5 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city9,
                            user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Rua Sao Marcos, 30, Gramado",
                            description="House",
                            squarefeet="1614 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city9,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

city10 = City(name="Recife",
              user_id="1")

session.add(city10)
session.commit()

immobileDetails1 = Immobile(address="Rua Ipiniras, 118, Recife",
                            description="House",
                            squarefeet="893 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="1 bathrooms",
                            city=city10,
                            user_id="1")

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address="Rua Capitao Araujo Miranda, 178, Recife",
                            description="House",
                            squarefeet="1808 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city10,
                            user_id="1")

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address="Rua Jader de Andrade, 125, Recife",
                            description="House",
                            squarefeet="4305 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="4 bathrooms",
                            city=city10,
                            user_id="1")

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address="Rua Ambrosio Machado, 210, Recife",
                            description="House",
                            squarefeet="753 squarefeet",
                            bedrooms="3 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city10,
                            user_id="1")

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address="Rua Itacaja, 66, Recife",
                            description="House",
                            squarefeet="4574 squarefeet",
                            bedrooms="4 bedrooms",
                            bathrooms="2 bathrooms",
                            city=city10,
                            user_id="1")

session.add(immobileDetails5)
session.commit()

print "address added!!"
