def convert_duration_to_hours(duration, unit):
    """Convertit la durée en heures selon l'unité choisie"""
    conversions = {
        "heures": 1,
        "jours": 24,
        "semaines": 24 * 7,
        "mois": 24 * 30
    }
    return duration * conversions.get(unit, 1)  # Par défaut, garde la même durée
