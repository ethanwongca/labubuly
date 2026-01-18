//
//  HomeView.swift
//  ios
//
//  Created by Sophia Xu on 2026-01-17.
//

import SwiftUI

struct HomeView: View {
    private var service = VoiceService()
    var body: some View {
        ZStack{
            Color.white
            Menu("Voice Picker") {
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
        }
        
    }
        

    func sendVoice(name: String) {
        Task {
            do {
                try await service.selectVoice(named: name)
            } catch {
                print ("selection failed")
            }
        }
    }
}


