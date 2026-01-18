//
//  HomeView.swift
//  ios
//
//  Created by Sophia Xu on 2026-01-17.
//

import SwiftUI

struct HomeView: View {
    private var service = VoiceService()
    @State private var selectedImage: String = "pinklabubu"
    var images = ["Default": "pinklabubu", "Breathy": "whitelabubu", "Deep": "graylabubu", "Whiny": "brownlabubu", "Screech": "pinklabubu"]
    var body: some View {
        ZStack{
            Color.white
            VStack{
                Image(selectedImage)
                    .resizable()
                    .aspectRatio(contentMode: .fit) // maintains aspect ratio within the frame
                    .frame(width: 200, height: 200)
                HStack{
                    Menu("Pick a voice") {
                        Button("Default") {
                            sendVoice(name: "Default")
                        }
                        Button("Breathy") {
                            sendVoice(name: "Breathy")
                        }
                        Button("Deep") {
                            sendVoice(name: "Deep")
                        }
                        Button("Whiny") {
                            sendVoice(name: "Whiny")
                        }
                        Button("Screech") {
                            sendVoice(name: "Screech")
                        }
                    }
                    
                    Image(systemName: "speaker.wave.3")
                        .symbolEffect(.bounce.up.byLayer, options: .repeat(3), value: selectedImage)
                        .font(.system(size: 30))
                }
                
                
            }
            
        }
        
    }
        

    func sendVoice(name: String) {
        Task {
            do {
                try await service.selectVoice(named: name)
            } catch {
                print ("voice selection failed")
            }
        }
        selectedImage = images[name]!
        
        
    }
}


