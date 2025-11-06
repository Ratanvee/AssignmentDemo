from rest_framework import serializers

class JobListingSerializer(serializers.Serializer):
    job_title = serializers.CharField(source='Job Title')
    location = serializers.CharField(source='Location')
    post_date = serializers.CharField(source='Post Date')
    job_link = serializers.URLField(source='Job Link')