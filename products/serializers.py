from rest_framework import serializers
from .models import Category, Product, Review, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id name products_count'.split()

    def get_products_count(self, obj):
        return obj.products.count()


class ProductSerializers(serializers.ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = 'id title description price category tag'.split()

    def validate_tags(self, value):
        existing_tags = Tag.objects.values_list('id', flat=True)
        for tag_id in value:
            if tag_id not in existing_tags:
                raise serializers.ValidationError(f"Tag with ID {tag_id} does not exist.")
        return value


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()


class ProductReviewSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'is_active', 'reviews', 'average_rating']
