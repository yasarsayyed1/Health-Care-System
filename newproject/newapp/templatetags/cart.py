from django import template


register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return True
    return False;

@register.filter(name="cart_count")
def cart_count(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    return False;


@register.filter(name="cart_total")
def cart_total(product,cart):
    return int(product.price) * int(cart_count(product,cart))

@register.filter(name="cart_sum")
def cart_sum(product,cart):
    sum=0;
    for p in product:
        sum+=cart_total(p,cart)
    return sum