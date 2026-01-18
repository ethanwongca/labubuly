//
//  BackgroundView.swift
//  ios
//
//  Created by Sophia Xu on 2026-01-17.
//

import SwiftUI
import AVKit

struct BackgroundView: UIViewRepresentable {
    var videoName: String
    var videoType: String
    func makeUIView(context: Context) -> AVPlayerView {
        AVPlayerView(frame: .zero, videoName: videoName, videoType: videoType)
    }
    
    func updateUIView(_ uiView: AVPlayerView, context: Context) {
    }
    
   
}

class AVPlayerView: UIView{
    var player: AVPlayer!
    var playerLayer: AVPlayerLayer!
    private var observer: Any?
    init(frame: CGRect, videoName: String, videoType: String) {
        super.init(frame: frame)
    
    guard let url = Bundle.main.url(forResource: videoName, withExtension: videoType) else { return }
    player = AVPlayer(url: url)
    playerLayer = AVPlayerLayer(player: player)
    playerLayer.videoGravity = .resizeAspectFill
    layer.addSublayer(playerLayer)
    observer = NotificationCenter.default.addObserver(forName: .AVPlayerItemDidPlayToEndTime, object: player.currentItem,queue: .main)
    { [weak self] _ in
                self?.player.seek(to: .zero)
                self?.player.play()
                
            }

            player.play()
        }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        playerLayer.frame = bounds
    }
    
    deinit {
        if let observer {
            NotificationCenter.default.removeObserver(observer)
        }
        player?.pause()
    }
    
  
    
            
    
}
