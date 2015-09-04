#!/usr/bin/env python

from troposphere import Base64, FindInMap, GetAtt, GetAZs, Join, If, Equals
from troposphere import Parameter, Output, Ref, Select, Tags, Template
import troposphere.ec2 as ec2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d','--delegation', required=True, type=str)
parser.add_argument('-k','--key', required=True, type=str)
args = parser.parse_args()

t=Template()

t.add_version('2010-09-09')
t.add_description('Test instance')

#PARAMETERS
KeyName = t.add_parameter(Parameter(
  "KeyName",
  Type = "String",
  Default = args.key,
  AllowedValues = [ args.key ],
  Description = "Key pair name"
))

InstanceType = t.add_parameter(Parameter(
  "InstanceType",
  Type = "String",
  Default = "t1.micro",
  AllowedValues = ["t1.micro"],
  Description = "Instance type"
))


#MAPPINGS
t.add_mapping("RegionMap", {
  "ap-southeast-1" : { "AMI" : "ami-9cbaeece" },
  "us-west-2"      : { "AMI" : "ami-36e2d473" },
  "us-west-1"      : { "AMI" : "ami-5820b868" }
})

#RESOURCES
inst=t.add_Resource(ec2.Instance(
  
)
