import asyncio
import websockets

rooms={}

async def chat_handler(websocket, path):
    try:
        room_name = await websocket.recv()
        if room_name not in rooms:
            rooms[room_name] = set()
        rooms[room_name].add(websocket)

        await asyncio.gather(
            *(client.send(f"A new user joined {room_name}") 
            for client in rooms[room_name] if client != websocket)
        )

        async for message in websocket:
            await asyncio.gather(
                *(client.send(f"[{room_name}] {message}")
                for client in rooms[room_name] if client != websocket
                )
            )
    
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected from room : {room_name}")
    finally:

        rooms[room_name].remove(websocket)
        if not rooms[room_name]:
            del rooms[room_name]

async def main():
    server = await websockets.serve(chat_handler, "localhost", 8765)
    print("Websocket server running on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main()) 