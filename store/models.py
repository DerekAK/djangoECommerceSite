from django.db import models

# Create your models here.
# use django field types on google (documentation)
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield

# one to one relationship between classes (written inside child class)
# parent_class_variable = models.OneToOneField(parent_class, on_delete=models.____, primary_key=True) 

# one to many relationship between classes (written inside child class)
# parent_class_variable = models.ForeignKey(parent_class, on_delete=models.____)

# many to many relationship between classes (written in either class)
# other_class_variable = models.ManyToMany(other_class)

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    
    # a featured_product can be associated with multiple collections
    # collection class depends on product class, and if go into product class, will see that product class depends on collection class
    # circular relationship, not ideal, but if necessary, need to put first argument in quotes because it is not defined above
    
    # related_name='+' tells django that we don't care about reverse relationship (because django will automatically create reverse relationship in corresponding class)
    # this will stop error that tells us there is a name clash
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255) #.CharField for short-medium strings
    description = models.TextField()
    # let's say max price is 9999.99
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) # use DecimalField, not FloatField, for monetary values
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    
    # a collection can have multiple products inside of it
    # don't want to delete products inside collection if delete collection
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    # a promotion can be associated with many products and vice versa
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEM_BRONZE = 'B'
    MEM_SILVER = 'S'
    MEM_GOLD = 'G'
    MEMBERSHIPS = [
        (MEM_BRONZE, 'Bronze'),    
        (MEM_SILVER, 'Silver'),
        (MEM_GOLD, 'Gold')
    ]
    membership = models.CharField(max_length=1, choices=MEMBERSHIPS, default=MEM_BRONZE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    # research django meta data
    class Meta:
        db_table = 'store_customer'
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]

class Order(models.Model):
    PAY_PENDING = 'P'
    PAY_COMPLETE = 'C'
    PAY_FAIL = 'F'
    PAYMENTS_STATUSES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Fail')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENTS_STATUSES, default=PAY_PENDING)
    # a customer can have multiple orders
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    # an order can have multiple orderItems
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # a product can have multiple orderItems associated with it
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    zip = models.IntegerField()
    # set up a one to one relationship between customer(parent) and address(child)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) 
    # on_delete means that if customer is deleted, so is address. Also need primary key to disallow duplicates

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    # a cart can have multiple cartItems
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # a product can be associated with many cartItems
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()