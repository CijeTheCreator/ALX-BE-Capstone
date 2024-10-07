from rest_framework import serializers
from .models import Product, Category, ProductImage

# Serializer for the Category model, handling the creation and representation of categories
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description']

# Serializer for the ProductImage model, handling the creation and representation of images
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image_id', 'image_url']

# Serializer for the Product model, handling the creation and representation of products
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'description', 'price', 'category', 'stock_quantity', 'created_date', 'images']

    def create(self, validated_data):
        # Extract nested category and images data
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images', [])

        # Create or get the category
        category, created = Category.objects.get_or_create(**category_data)

        # Create the product
        product = Product.objects.create(category=category, **validated_data)

        # Handle the images
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)

        return product
    
    def update(self, instance, validated_data):
        # Extract nested category and images data
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images', [])

        # Update the category (assuming categories are not created through PUT)
        category, created = Category.objects.get_or_create(**category_data)
        instance.category = category

        # Update the product fields
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.stock_quantity = validated_data.get('stock_quantity', instance.stock_quantity)
        instance.save()

        # Clear existing images and add new ones
        instance.images.clear()  # Or delete and recreate images if necessary
        for image_data in images_data:
            ProductImage.objects.create(product=instance, **image_data)

        return instance

