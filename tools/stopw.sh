#!/usr/bin/env bash
i_id=$(aws ec2 describe-instances --filters 'Name=tag:Name,Values=w' | jq -r .Reservations[0].Instances[0].InstanceId)
aws ec2 stop-instances --instance-ids  $i_id
