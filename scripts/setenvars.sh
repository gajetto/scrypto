#!/bin/bash

file=$HOME/.bashrc
if ! grep -q AWS_ACCESS_KEY "$file"; then
cat >> /home/ec2-user/.bashrc <<EOF
export AWS_ACCESS_KEY_ID='AKIAIDR5KOXQ7UTVHN2Q'
export AWS_SECRET_ACCESS_KEY='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'
export AWS_DEFAULT_REGION='eu-west-2'
export access_token_key='860424992-naN5HsbWjT2H6x8OGpRvhmIlcNlT4oKAQP4T8KbL'
export access_token_secret='4ll6nduMmVGp29pYypd6lvepQrCZKMoWwWgKryg6Y4C04'
export consumer_key='Hl5rwZKwvh96gh6elqEnTd4gK'
export consumer_secret='jjzm0Mz3vCSq6dNDGroNudvXMYpnzrZQQFldv3vUnjBESiFUf1'
export telepot_token='461226220:AAG-QSiVeUqn5uuC4JVxCyIkI2pJeyrRqPo'
export VBIN='/home/ec2-user/env/scrypto/bin'
export VBASE='/home/ec2-user/env/scrypto'
EOF
fi

source ~/.bashrc
source /home/ec2-user/env/scrypto/bin/activate
sudo chown -R ec2-user:ec2-user /var/www/scrypto/