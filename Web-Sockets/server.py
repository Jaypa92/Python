import asyncio
import websockets

async def echo(websocket, path):
    print(f"New connection from {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed with error: {e}")

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server rinning on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())