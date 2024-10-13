_mapping = {
    "Anser indicus": ("Oie à tête barrée", "Bar-headed goose", "Горный гусь"),
    "Phalacrocorax carbo": ("Grand Cormoran", "Great cormorant", "Большой баклан"),
    "Aix galericulata": ("Canard mandarin", "Mandarin duck", "Мандаринка"),
    "Ardea cinerea": ("Héron cendré", "Grey heron", "Серая цапля"),
    "Pavo cristatus": ("Paon bleu", "Indian peafowl", "Обыкновенный павлин"),
    "Sturnus": ("Sturnus", "Sturnus", "Скворeц"),
    "Cygnus": ("Cygne", "Swan", "Лебедь"),
    "Cygnus olor": ("Cygne tuberculé", "Mute swan", "Лебедь-шипун"),
    "Gallinula chloropus": ("Gallinule poule-d'eau", "Common moorhen", "Камышница"),
    "Laridae": ("Larinae", "Gull", "Чайка"),
    "Phalacrocorax": ("Cormoran", "Cormorant", "Баклан"),
    "Fulica atra": ("Foulque macroule", "Eurasian coot", "Лысуха"),
    "Corvus corax": ("Grand corbeau", "Common raven", "Ворон"),
    "Columba": ("Pigeon", "Pigeon", "Голубь"),
    "Anser anser": ("Oie cendrée", "Greylag goose", "Серый гусь"),
    "Chroicocephalus ridibundus": (
        "Mouette rieuse",
        "Black-headed gull",
        "Озёрная чайка",
    ),
    "Psittacula krameri": (
        "Perruche à collier",
        "Rose-ringed parakeet",
        "Индийский кольчатый попугай",
    ),
    "Turdus merula": ("Merle noir", "Common blackbird", "Чёрный дрозд"),
    "Unknown": ("???", "???", "???"),
}


def translate(latin_name: str) -> tuple[str, str, str]:
    if latin_name in _mapping:
        return _mapping[latin_name]
    print(f"No translation for {latin_name}")
    return "", "", ""
