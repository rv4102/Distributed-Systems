from flask import Flask, jsonify, request
from mysql.connector.errors import Error
from SQLHandler import SQLHandler
import aiohttp
import os

app = Flask(__name__)
# sql = SQLHandler()


shard_to_log_count = {}

@app.route('/get_log_count', methods=['GET'])
def get_log_count():
    payload = request.get_json()
    shard = payload.get('shard')
    return jsonify({"count": shard_to_log_count[shard], "status": "success"}), 200

@app.route('/set_log_count', methods=['POST'])
def set_log_count():
    payload = request.get_json()
    shard = payload.get('shard')
    count = payload.get('count')
    shard_to_log_count[shard] = count
    return jsonify({"message": f"Log count for {shard} set to {count}", "status": "success"}), 200



# s1 7 
# s2 8 
# s3 6 dead
# s4 10 primary














# server_name = os.environ['SERVER_NAME']
# server_name = 'server1'
# primary_shards = [] 
# logfile = []
# shard_to_logcount = {}

# async def get_shard_servers(shard_id):
#     async with aiohttp.ClientSession() as session:
#         payload = {"shard": shard_id}
#         async with session.post(f'http://localhost:5000/get_shard_servers', json=payload) as resp:
#             if resp.status == 200:
#                 return await resp.json()
#             else:
#                 return None

# async def write_shard_data(serverName, shard, data):
#     async with aiohttp.ClientSession() as session:
#         payload = {"shard": shard, "data": data}
#         async with session.post(f'http://{serverName}:5000/write', json=payload) as resp:
#             if resp.status == 200:
#                 return True
#             else:
#                 return False

# async def update_shard_data(serverName, shard, Stud_id, data):
#     async with aiohttp.ClientSession() as session:
#         payload = {"shard": shard, "Stud_id": Stud_id, "data": data}
#         async with session.put(f'http://{serverName}:5000/update', json=payload) as resp:
#             if resp.status == 200:
#                 return True
#             else:
#                 return False

# async def delete_shard_data(serverName, shard, Stud_id):
#     async with aiohttp.ClientSession() as session:
#         payload = {"shard": shard, "Stud_id": Stud_id}
#         async with session.delete(f'http://{serverName}:5000/del', json=payload) as resp:
#             if resp.status == 200:
#                 return True
#             else:
#                 return False

# @app.route('/config', methods=['POST'])
# def configure_server():
#     payload = request.get_json()
#     schema = payload.get('schema')
#     shards = payload.get('shards')

#     if not schema or not shards:
#         return jsonify({"message": "Invalid payload", "status": "error"}), 400

#     if 'columns' not in schema or 'dtypes' not in schema or len(schema['columns']) != len(schema['dtypes']) or len(schema['columns']) == 0:
#         return jsonify({"message": "Invalid schema", "status": "error"}), 400

#     for shard in shards:
#         sql.UseDB(dbname=shard)
#         sql.CreateTable(
#             tabname='studT', columns=schema['columns'], dtypes=schema['dtypes'], prikeys=['Stud_id'])

#     response_message = f"{', '.join(f'{server_name}:{shard}' for shard in shards)} configured"
#     response_data = {"message": response_message, "status": "success"}

#     return jsonify(response_data), 200


# @app.route('/copy', methods=['GET'])
# def copy_data():
#     payload = request.get_json()
#     shards = payload.get('shards')

#     if not shards:
#         return jsonify({"message": "Invalid payload", "status": "error"}), 400

#     response_data = {}
#     for shard in shards:
#         if not sql.hasDB(dbname=shard):
#             return jsonify({"message": f"{server_name}:{shard} not found", "status": "error"}), 404
#         sql.UseDB(dbname=shard)
#         response_data[shard] = sql.Select(table_name='studT')
#     response_data["status"] = "success"

#     return jsonify(response_data), 200


# @app.route('/read', methods=['POST'])
# def read_data():
#     payload = request.get_json()
#     shard = payload.get('shard')
#     Stud_id = payload.get('Stud_id')

#     if not shard or not Stud_id or 'low' not in Stud_id or 'high' not in Stud_id:
#         return jsonify({"message": "Invalid payload", "status": "error"}), 400

#     if not sql.hasDB(dbname=shard):
#         return jsonify({"message": f"{server_name}:{shard} not found", "status": "error"}), 404

#     sql.UseDB(dbname=shard)
#     data = sql.Select(table_name="studT", col="Stud_id",
#                       low=Stud_id['low'], high=Stud_id['high'])

#     response_data = {"data": data, "status": "success"}

#     return jsonify(response_data), 200


# @app.route('/write', methods=['POST'])
# def write_data():
#     payload = request.get_json()
#     shard = payload.get('shard')
#     data = payload.get('data')

#     if not shard or not data:
#         return jsonify({"message": "Invalid payload", "status": "error"}), 400

#     if not sql.hasDB(dbname=shard):
#         return jsonify({"message": f"{server_name}:{shard} not found", "status": "error"}), 404
    
#     # this server is a primary server if shard is in primary_shards
#     logfile.append(f"ADD {shard}, {data['Stud_id']}, {data['Stud_name']}, {data['Stud_marks']}")
#     shard_to_logcount[shard] = shard_to_logcount.get(shard, 0) + 1
#     if shard in primary_shards:
#         servers = get_shard_servers(shard)
#         if servers is None:
#             return jsonify({"message": f"Error in getting servers for {shard}", "status": "error"}), 500
#         for server in servers:
#             if server == server_name:
#                 continue
#             response = write_shard_data(server, shard, data)
#             if response is False:
#                 return jsonify({"message": f"Error in writing data to {server}", "status": "error"}), 500 

#     sql.UseDB(dbname=shard)
#     sql.Insert(table_name='studT', rows=data)

#     response_data = {"message": "Data entries added", "status": "success"}
#     return jsonify(response_data), 200


# @app.route('/update', methods=['PUT'])
# def update_data():
#     payload = request.get_json()
#     shard = payload.get('shard')
#     Stud_id = payload.get('Stud_id')
#     data = payload.get('data')

#     if not shard or Stud_id is None or not data:
#         return jsonify({"message": "Invalid payload", "status": "error"}), 400

#     if not sql.hasDB(dbname=shard):
#         return jsonify({"message": f"{server_name}:{shard} not found", "status": "error"}), 404

#     logfile.append(f"UPDATE {shard}, {Stud_id}, {data['Stud_name']}, {data['Stud_marks']}")
#     shard_to_logcount[shard] = shard_to_logcount.get(shard, 0) + 1
#     if shard in primary_shards:
#         servers = get_shard_servers(shard)
#         if servers is None:
#             return jsonify({"message": f"Error in getting servers for {shard}", "status": "error"}), 500
#         for server in servers:
#             if server == server_name:
#                 continue
#             response = update_shard_data(server, shard, Stud_id, data)
#             if response is False:
#                 return jsonify({"message": f"Error in writing data to {server}", "status": "error"}), 500
    
#     sql.UseDB(dbname=shard)
#     if not sql.Exists(table_name='studT', col="Stud_id", val=Stud_id):
#         return jsonify({"message": f"Data entry for Stud_id:{Stud_id} not found", "status": "error"}), 404
#     sql.Update(table_name='studT', col="Stud_id", val=Stud_id, data=data)

#     response_data = {
#         "message": f"Data entry for Stud_id:{Stud_id} updated", "status": "success"
#     }

#     return jsonify(response_data), 200


# @app.route('/del', methods=['DELETE'])
# def delete_data():
#     payload = request.get_json()
#     shard = payload.get('shard')
#     Stud_id = payload.get('Stud_id')

#     if not shard or Stud_id is None:
#         return jsonify({"message": "Invalid payload", "status": "error"}), 400

#     if not sql.hasDB(dbname=shard):
#         return jsonify({"message": f"{server_name}:{shard} not found", "status": "error"}), 404

#     logfile.append(f"DELETE {shard}, {Stud_id}")
#     shard_to_logcount[shard] = shard_to_logcount.get(shard, 0) + 1
#     if shard in primary_shards:
#         servers = get_shard_servers(shard)
#         if servers is None:
#             return jsonify({"message": f"Error in getting servers for {shard}", "status": "error"}), 500
#         for server in servers:
#             if server == server_name:
#                 continue
#             response = delete_shard_data(server, shard, Stud_id)
#             if response is False:
#                 return jsonify({"message": f"Error in writing data to {server}", "status": "error"}), 500

#     sql.UseDB(dbname=shard)
#     if not sql.Exists(table_name='studT', col="Stud_id", val=Stud_id):
#         return jsonify({"message": f"Data entry for Stud_id:{Stud_id} not found", "status": "error"}), 404
#     sql.Delete(table_name='studT', col="Stud_id", val=Stud_id)

#     response_data = {
#         "message": f"Data entry with Stud_id:{Stud_id} removed", "status": "success"}

#     return jsonify(response_data), 200

# @app.route('/get_log_count', methods=['GET'])
# def get_log_count():
#     payload = request.get_json()
#     shard = payload.get('shard')
#     return jsonify({"count": shard_to_logcount[shard], "status": "success"}), 200

# @app.route('/heartbeat', methods=['GET'])
# def heartbeat():
#     return '', 200


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Exception: {e}")
    if isinstance(e, Error):
        return jsonify({"message": e.msg, "status": "error"}), 400
    else:
        return jsonify({"message": "Internal server Error: check params", "status": "error"}), 500

@app.before_request
async def startup():
    app.logger.info("Starting metadata server...")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)