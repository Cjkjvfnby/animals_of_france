_mapping = {
    "Anser indicus": ("Oie à tête barrée", "Bar-headed goose", "Горный гусь"),
    "Phalacrocorax carbo": ("Grand Cormoran", "Great cormorant", "Большой баклан"),
    "Aix galericulata": ("Canard mandarin", "Mandarin duck", "Мандаринка"),
    "Ardea cinerea": ("Héron cendré", "Grey heron", "Серая цапля"),
    "Pavo cristatus": ("Paon bleu", "Indian peafowl", "Обыкновенный павлин"),
}


def translate(latin_name: str) -> tuple[str, str, str]:
    return _mapping.get(latin_name, ("", "", ""))
