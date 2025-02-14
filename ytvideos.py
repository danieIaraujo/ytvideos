"""Tool com rastreador de vídeos já baixados anteriormente"""
from yt_dlp import YoutubeDL                                                                                

# Patch para corrigir o erro 403
def apply_patch():
    import yt_dlp
    yt_dlp.utils.bug_reports_message = lambda: ''  # Desativa mensagens de bugs
    yt_dlp.utils.update_ydl_info = lambda *args, **kwargs: None  # Ignora atualizações
    yt_dlp.utils.std_headers = {  # Define headers personalizados
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Sec-Fetch-Mode': 'navigate',
    }

# Função para baixar vídeos
def baixar_video(link):
    try:
        # Configurações do yt-dlp
        ydl_opts = {
            'format': 'best',  # Baixa a melhor qualidade disponível
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Salva na pasta "downloads"
            'download_archive': 'downloads/baixados.txt',  # Rastreia vídeos já baixados
        }

        # Aplica o patch
        apply_patch()

        # Baixa o vídeo
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print("Download concluído ou vídeo já baixado anteriormente!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função principal
if __name__ == "__main__":
    # Solicita o link do vídeo
    link = input("Cole o link do vídeo do YouTube: ")

    # Chama a função para baixar o vídeo
    baixar_video(link)
