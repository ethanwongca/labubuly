//
//  NetworkConnection.swift
//  Connects our SwiftUI to the Fast API
//

import Foundation
import Combine


struct VoiceRequest: Codable, Sendable {
    let name: String
}

class VoiceService: ObservableObject {

    func selectVoice(named voiceName: String) async throws -> String {
        guard let url = URL(string: "<endpoint>selected_voice") else {
            throw URLError(.badURL)
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let voiceRequest = VoiceRequest(name: voiceName)
        request.httpBody = try JSONEncoder().encode(voiceRequest)
        
        let (data, response) = try await URLSession.shared.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw URLError(.badServerResponse)
        }
        
        guard let voiceID = String(data: data, encoding: .utf8) else {
            throw URLError(.cannotDecodeContentData)
        }
        
        return voiceID
    }
}
