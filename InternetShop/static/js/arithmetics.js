let total_price = 0;

function find_product_price(price, count) {
    total_price += price * count;
    document.write(price * count);
}