from flask import Flask, request, Response,jsonify
import os
import boto3
import json
import botocore
from werkzeug import secure_filename
from botocore.exceptions import ClientError
app = Flask(__name__)
s3 = boto3.client('s3')


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/downloads3/<bucket>/<key>", methods=['GET'])
def downloads3(bucket, key):
    url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': bucket,
        'Key': key
        }
)

    return (url)


@app.route("/uploads3/<bucket>", methods=['POST'])
def uploads3(bucket):
    file = request.files['file']
    filename = secure_filename(file.filename)
    s3 = boto3.client('s3')
    try:
        s3.upload_fileobj(file, bucket, filename)
        return ("archivo subido")
    except botocore.exceptions.ClientError as e:
        return("El bucket no existe")


@app.route("/listfiles/<bucket>", methods=['GET'])
def listfiles(bucket):
    s3 = boto3.client('s3')
    s3.list_objects_v2(Bucket=bucket)
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return jsonify(keys)

@app.route("/deletefile/<bucket>/<key>", methods=['GET'])
def deletefile(bucket, key):
    client = boto3.client('s3')
    client.delete_object(Bucket=bucket, Key=key)
    return("Archivo eliminado")



app.run(host ='0.0.0.0')

