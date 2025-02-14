"""Tool com rastreador de vídeos já baixados anteriormente"""
from yt_dlp import YoutubeDL

def baixar_video(link):
    try:
        # Configurações do yt-dlp
        ydl_opts = {'format': 'best',  # Baixa a melhor qualidade disponível
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Salva na pasta "downloads"
            'download_archive': 'downloads/baixados.txt',}  # Arquivo para rastrear vídeos baixados
        
        # Cria o procedimento configurado YoutubeDL com as opções
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])  # Baixa o vídeo

        print("Download concluído ou vídeo já baixado anteriormente!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    link = input("Cole o link do vídeo do YouTube: ")
    baixar_video(link)
