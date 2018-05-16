def serialize_recipe(recipe):
    return {
        'title': recipe['id'],
        'isVegetarian': recipe['isVegetarian'],
        'url': recipe['url'],
        'image': recipe['image'],
        'serves': recipe['serves'],
        'recommendations': recipe['recommendations'],
    }
