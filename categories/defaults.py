from categories.models.category_models import CategoryColor, CategoryIcon, CategoryType

DEFAULT_CATEGORIES = [
    # RECEITAS
    {
        "name": "Trabalho",
        "category_type": CategoryType.INCOME,
        "category_color": CategoryColor.GREEN,
        "category_icon": CategoryIcon.BRIEFCASE,
    },
    {
        "name": "Investimentos",
        "category_type": CategoryType.INCOME,
        "category_color": CategoryColor.DARKGREEN,
        "category_icon": CategoryIcon.TRENDINGUP,
    },
    {
        "name": "Freelance",
        "category_type": CategoryType.INCOME,
        "category_color": CategoryColor.GREEN,
        "category_icon": CategoryIcon.LAPTOP
    },

    # DESPESAS
    {
        "name": "Moradia",
        "category_type": CategoryType.EXPENSE,
        "category_color": CategoryColor.BLUE,
        "category_icon": CategoryIcon.HOME,
    },
    {
        "name": "Alimentação",
        "category_type": CategoryType.EXPENSE,
        "category_color": CategoryColor.ORANGE,
        "category_icon": CategoryIcon.UTENSILS,
    },
    {
        "name": "Transporte",
        "category_type": CategoryType.EXPENSE,
        "category_color": CategoryColor.BROWN,
        "category_icon": CategoryIcon.BUS,
    },
    {
        "name": "Serviços",
        "category_type": CategoryType.EXPENSE,
        "category_color": CategoryColor.GRAY,
        "category_icon": CategoryIcon.WRENCH,
    },
    {
        "name": "Saúde",
        "category_type": CategoryType.EXPENSE,
        "category_color": CategoryColor.RED,
        "category_icon": CategoryIcon.HEARTPULSE
    },
    {
        "name": "Lazer",
        "category_type": CategoryType.EXPENSE,
        "category_color": CategoryColor.PURPLE,
        "category_icon": CategoryIcon.PARTYPOPPER
    }
]