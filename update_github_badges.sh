#!/bin/bash

STARS_CURL=$(curl -s https://api.github.com/repos/gyulyvgc/sniffnet --header "Authorization: Bearer $GH_API_TOKEN")
echo "---> STARS_CURL: $STARS_CURL"
STARS_COUNT=$(echo "$STARS_CURL" | grep -E -o '"stargazers_count": [0-9]*' | head -1 | cut '-d:' -f 2 | tr -d ' ')
echo "---> STARS_COUNT: $STARS_COUNT"

FOLLOWERS_CURL=$(curl -s https://api.github.com/users/GyulyVGC --header "Authorization: Bearer $GH_API_TOKEN")
echo "---> FOLLOWERS_CURL: $FOLLOWERS_CURL"
FOLLOWERS_COUNT=$(echo "$FOLLOWERS_CURL" | grep -E -o '"followers": [0-9]*' | head -1 | cut '-d:' -f 2 | tr -d ' ')
echo "---> FOLLOWERS_COUNT: $FOLLOWERS_COUNT"

VERSION_CURL=$(curl -s https://api.github.com/repos/gyulyvgc/sniffnet/releases/latest --header "Authorization: Bearer $GH_API_TOKEN")
echo "---> VERSION_CURL: $VERSION_CURL"
VERSION_TAG=$(echo "$VERSION_CURL" | grep -E -o '"tag_name": "[^"]*"' | head -1 | cut '-d"' -f 4)
VERSION_STRING=$(echo "$VERSION_TAG" | tr '[:lower:]' '[:upper:]')
echo "---> VERSION_STRING: $VERSION_STRING"

if [ $STARS_COUNT -ge 10000 ]; then
    FLOAT=$(bc -l <<< "$STARS_COUNT/1000")
    STARS_STRING=$(printf "%.0f" $FLOAT)k
elif [ $STARS_COUNT -ge 1000 ]; then
    FLOAT=$(bc -l <<< "$STARS_COUNT/1000")
    STARS_STRING=$(printf "%.1f" $FLOAT)k
else
    STARS_STRING=$STARS_COUNT
fi
echo "STARS_STRING: $STARS_STRING"

STARS_STRING_UPPER=$(echo "$STARS_STRING" | tr '[:lower:]' '[:upper:]')
echo "STARS_STRING_UPPER: $STARS_STRING_UPPER"

if [ $FOLLOWERS_COUNT -ge 10000 ]; then
    FLOAT=$(bc -l <<< "$FOLLOWERS_COUNT/1000")
    FOLLOWERS_STRING=$(printf "%.0f" $FLOAT)k
elif [ $FOLLOWERS_COUNT -ge 1000 ]; then
    FLOAT=$(bc -l <<< "$FOLLOWERS_COUNT/1000")
    FOLLOWERS_STRING=$(printf "%.1f" $FLOAT)k
else
    FOLLOWERS_STRING=$FOLLOWERS_COUNT
fi
echo "FOLLOWERS_STRING: $FOLLOWERS_STRING"

if ! [[ $STARS_STRING =~ ^[1-9][0-9]{0,2}(\.[0-9])?k?$ ]] ; then
    echo "Error: Invalid format for STARS_STRING"
    exit 1
fi

if ! [[ $FOLLOWERS_STRING =~ ^[1-9][0-9]{0,2}(\.[0-9])?k?$ ]] ; then
    echo "Error: Invalid format for FOLLOWERS_STRING"
    exit 1
fi

if ! [[ $VERSION_STRING =~ ^V[0-9]+(\.[0-9]+)*$ ]] ; then
    echo "Error: Invalid format for VERSION_STRING"
    exit 1
fi

sed "s/REPLACE_ME/$STARS_STRING_UPPER/g" assets/img/badges/stars_badge_template.svg > assets/img/badges/stars_badge.svg
sed "s/REPLACE_ME/$STARS_STRING/g" assets/img/badges/stars_social_badge_template.svg > assets/img/badges/stars_social_badge.svg
sed "s/REPLACE_ME/$FOLLOWERS_STRING/g" assets/img/badges/followers_badge_template.svg > assets/img/badges/followers_badge.svg
sed "s/REPLACE_ME/$VERSION_STRING/g" assets/img/badges/version_badge_template.svg > assets/img/badges/version_badge.svg

exit 0