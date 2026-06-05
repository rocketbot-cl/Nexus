# coding: utf-8
"""
Módulo de integración con Nexus API.
Permite leer/escribir datos en tablas y escuchar eventos en tiempo real vía WebSocket.

Para obtener el módulo/función que se está llamando:
    GetParams("module")

Para obtener variables enviadas desde el formulario/comando:
    var = GetParams(variable)

Para modificar una variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)
"""

import sys
import os
import json

BASE_PATH = tmp_global_obj["basepath"]  # type: ignore
cur_path = BASE_PATH + "modules" + os.sep + "Nexus" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

import requests

GetGlobals = GetGlobals # type: ignore
GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore


module = GetParams("module")
session = GetParams("session") or "default"

global mod_nx_session

try:
    if not mod_nx_session: #type:ignore
        mod_nx_session = {}
except NameError:
    mod_nx_session = {}

global _session_data, _require_session, _headers, _json, _check

def _session_data():
    return mod_nx_session.get(session) or {}

def _require_session():
    data = _session_data()
    if not data.get("base_url"):
        raise RuntimeError(
            f"Session '{session}' not initialized. "
            "Run 'Connect to Nexus' first."
        )
    return data

def _headers(data):
    return {
        "Content-Type": "application/json",
        "X-API-Key": data["api_key"],
    }

def _json(resp):
    try:
        return resp.json()
    except Exception:
        return None

def _check(resp):
    data = _json(resp)

    if 200 <= resp.status_code < 300:
        return data if data is not None else resp.text

    if isinstance(data, dict):
        msg = data.get("error") or data.get("message") or str(data)
    else:
        msg = resp.text[:1000]

    raise RuntimeError(
        f"Nexus error in '{module}': HTTP {resp.status_code} - {msg} - URL: {resp.url}"
    )


if module == "connectRocketview":
    try:
        base_url = (GetParams("base_url") or "").rstrip("/")
        api_key = GetParams("api_key")
        result_var = GetParams("result_var")

        if not base_url:
            raise ValueError("Base URL is required.")
        if not api_key:
            raise ValueError("API Key is required.")

        resp = requests.get(
            f"{base_url}/api/v1/external/tables",
            headers={"X-API-Key": api_key},
            timeout=10,
        )
        if resp.status_code not in (200, 201):
            raise ConnectionError(
                f"Connection failed: HTTP {resp.status_code} – {resp.text[:300]}"
            )

        mod_nx_session[session] = {"base_url": base_url, "api_key": api_key}
        if result_var:
            SetVar(result_var, True)

    except Exception as e:
        PrintException()
        raise e

if module == "listTables":
    try:
        data = _require_session()
        result_var = GetParams("result_var")

        resp = requests.get(
            f"{data['base_url']}/api/v1/external/tables",
            headers=_headers(data),
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "getTable":
    try:
        data = _require_session()
        table_id = GetParams("table_id")
        result_var = GetParams("result_var")

        resp = requests.get(
            f"{data['base_url']}/api/v1/external/tables/{table_id}",
            headers=_headers(data),
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "createTable":
    try:
        data = _require_session()
        table_data = GetParams("table_data")
        result_var = GetParams("result_var")

        if isinstance(table_data, str):
            table_data = json.loads(table_data)

        resp = requests.post(
            f"{data['base_url']}/api/v1/external/tables",
            headers=_headers(data),
            json=table_data,
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "updateTable":
    try:
        data = _require_session()
        table_id = GetParams("table_id")
        table_data = GetParams("table_data")
        result_var = GetParams("result_var")

        if isinstance(table_data, str):
            table_data = json.loads(table_data)

        resp = requests.put(
            f"{data['base_url']}/api/v1/external/tables/{table_id}",
            headers=_headers(data),
            json=table_data,
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "deleteTable":
    try:
        data = _require_session()
        table_id = GetParams("table_id")
        result_var = GetParams("result_var")

        resp = requests.delete(
            f"{data['base_url']}/api/v1/external/tables/{table_id}",
            headers=_headers(data),
            timeout=15,
        )
        _check(resp)
        if result_var:
            SetVar(result_var, True)

    except Exception as e:
        PrintException()
        raise e
    
if module == "getRows":
    try:
        data = _require_session()
        table_id = GetParams("table_id")
        limit = int(GetParams("limit") or 100)
        offset = int(GetParams("offset") or 0)
        result_var = GetParams("result_var")

        resp = requests.get(
            f"{data['base_url']}/api/v1/external/tables/{table_id}/rows",
            headers=_headers(data),
            params={"limit": limit, "offset": offset},
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "insertRow":
    try:
        data = _require_session()
        table_id = GetParams("table_id")
        row_data = GetParams("row_data")
        result_var = GetParams("result_var")

        if isinstance(row_data, str):
            row_data = json.loads(row_data)

        resp = requests.post(
            f"{data['base_url']}/api/v1/external/tables/{table_id}/rows",
            headers=_headers(data),
            json=row_data,
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "updateRow":
    try:
        data = _require_session()
        row_id = GetParams("row_id")
        row_data = GetParams("row_data")
        result_var = GetParams("result_var")

        if isinstance(row_data, str):
            row_data = json.loads(row_data)

        resp = requests.put(
            f"{data['base_url']}/api/v1/external/rows/{row_id}",
            headers=_headers(data),
            json=row_data,
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "deleteRow":
    try:
        data = _require_session()
        row_id = GetParams("row_id")
        result_var = GetParams("result_var")

        resp = requests.delete(
            f"{data['base_url']}/api/v1/external/rows/{row_id}",
            headers=_headers(data),
            timeout=15,
        )
        _check(resp)
        if result_var:
            SetVar(result_var, True)

    except Exception as e:
        PrintException()
        raise e

if module == "deleteAllRows":
    try:
        data = _require_session()
        table_id = GetParams("table_id")
        result_var = GetParams("result_var")

        resp = requests.delete(
            f"{data['base_url']}/api/v1/external/tables/{table_id}/rows",
            headers=_headers(data),
            timeout=15,
        )
        _check(resp)
        if result_var:
            SetVar(result_var, True)

    except Exception as e:
        PrintException()
        raise e

if module == "updateCell":
    try:
        data = _require_session()
        table_id = GetParams("table_id")
        row_id = GetParams("row_id")
        column = GetParams("column")
        value = GetParams("value")
        result_var = GetParams("result_var")

        resp = requests.put(
            f"{data['base_url']}/api/v1/external/tables/{table_id}/rows/{row_id}/cells/{column}",
            headers=_headers(data),
            json={"value": value},
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e

if module == "listQueries":
    try:
        data = _require_session()
        result_var = GetParams("result_var")

        resp = requests.get(
            f"{data['base_url']}/api/v1/external/queries",
            headers=_headers(data),
            timeout=15,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e
    
if module == "executeQuery":
    try:
        data = _require_session()
        query_id = GetParams("query_id")
        parameters = GetParams("parameters") or {}
        result_var = GetParams("result_var")

        if isinstance(parameters, str):
            parameters = json.loads(parameters)

        resp = requests.post(
            f"{data['base_url']}/api/v1/external/queries/{query_id}/execute",
            headers=_headers(data),
            json={"parameters": parameters},
            timeout=30,
        )

        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "connectWebSocket":
    try:
        try:
            import socketio as _sio_lib
        except ImportError:
            raise ImportError(
                "Package 'python-socketio[client]' not installed. "
                "Run:  pip install \"python-socketio[client]\" websocket-client -t libs/"
            )

        data       = _require_session()
        app_id     = GetParams("app_id")
        result_var = GetParams("result_var")

        events_buffer = []
        sio = _sio_lib.Client(logger=False, engineio_logger=False)

        @sio.on("db:change")
        def _on_db_change(event_data):
            events_buffer.append(event_data)

        @sio.event
        def connect():
            sio.emit("join:app", app_id)

        sio.connect(
            data["base_url"],
            headers={"X-API-Key": data["api_key"]},
            transports=["websocket"],
        )

        current = _session_data()
        current["_sio"]    = sio
        current["_events"] = events_buffer
        nx[session] = current

        if result_var:
            SetVar(result_var, True)

    except Exception as e:
        PrintException()
        raise e


if module == "getPendingEvents":
    try:
        clear = GetParams("clear")
        result_var = GetParams("result_var")

        current = _session_data()
        events  = list(current.get("_events") or [])

        if result_var:
            SetVar(result_var, events)

        if str(clear).lower() in ("true", "1", "yes"):
            buf = current.get("_events")
            if buf is not None:
                buf.clear()

    except Exception as e:
        PrintException()
        raise e


if module == "disconnectWebSocket":
    try:
        result_var = GetParams("result_var")
        current = _session_data()
        sio = current.get("_sio")

        if sio:
            try:
                sio.disconnect()
            except Exception:
                pass
            current.pop("_sio", None)
            current.pop("_events", None)
            nx[session] = current

        if result_var:
            SetVar(result_var, True)

    except Exception as e:
        PrintException()
        raise e


if module == "executeInternalQuery":
    try:
        data = _require_session()
        query_id = GetParams("query_id")
        parameters = GetParams("parameters") or {}
        jwt_token = GetParams("jwt_token") or ""
        result_var = GetParams("result_var")

        if isinstance(parameters, str):
            parameters = json.loads(parameters)

        if not jwt_token:
            raise ValueError("The 'jwt_token' parameter is required for the internal API.")

        resp = requests.post(
            f"{data['base_url']}/api/v1/query/{query_id}/execute",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {jwt_token}",
            },
            json={"parameters": parameters},
            timeout=30,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "executeApiCall":
    try:
        data = _require_session()
        apicall_id = GetParams("apicall_id")
        parameters = GetParams("parameters") or {}
        jwt_token = GetParams("jwt_token") or ""
        result_var = GetParams("result_var")

        if isinstance(parameters, str):
            parameters = json.loads(parameters)

        if not jwt_token:
            raise ValueError("The 'jwt_token' parameter is required for the internal API.")

        resp = requests.post(
            f"{data['base_url']}/api/v1/apicall/{apicall_id}/execute",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {jwt_token}",
            },
            json={"parameters": parameters},
            timeout=30,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


if module == "executeFunction":
    try:
        data = _require_session()
        function_id = GetParams("function_id")
        parameters = GetParams("parameters") or {}
        context = GetParams("context") or {}
        jwt_token = GetParams("jwt_token") or ""
        result_var = GetParams("result_var")

        if isinstance(parameters, str):
            parameters = json.loads(parameters)

        if isinstance(context, str):
            context = json.loads(context)

        if not jwt_token:
            raise ValueError("The 'jwt_token' parameter is required for the internal API.")

        resp = requests.post(
            f"{data['base_url']}/api/v1/functions/{function_id}/execute",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {jwt_token}",
            },
            json={"parameters": parameters, "context": context},
            timeout=30,
        )
        result = _check(resp)
        if result_var:
            SetVar(result_var, result)

    except Exception as e:
        PrintException()
        raise e


